1. Создаём проект
    1. `pip3 install scrapy`
    2. `cd <где будем создавать проект>`
    3. `scrapy startproject eupropegym`
    4. `scrapy genspider pricelist europegym.ru`
    5. Файл спайдера — `europegym/spiders/pricelist.py`
2. Привязываемся к странице со списком
    1. Находим точку входа: `https://www.europegym.ru/centers/prices/1.html`
    2. Вставляем в `start_urls` спайдера
    3. Запускаем через `scrapy crawl pricelist`.
    4. Замечаем, что скрепи ругается на `robots.txt`. В `settings.py` меняем `ROBOTSTXT_OBEY = True` на `ROBOTSTXT_OBEY = False`.
3. Находим список ссылок, которые нужно обойти
    1. Находим глазами, где нужные данные
    2. Смотрим на это место через инспектор (пракая кнопка — простотреть код)
    3. Придумываем селектор и вызываем его в консоли через `$$(<selector>)`, пока не получится что надо — `.side_info:last-child a`
4. Приделываем обход ссылок в спайдера `PricelistSpider.parse`: `for link in response.css('.side_info:last-child a'):`
    1. В цикле извлекаем из ссылок адрес, на который она ведёт: `link.css('::attr(href)').extract_first()`
    2. Смотрим, собрались ли нужные адреса:
    ```
    href = link.css('::attr(href)').extract_first()
    yield { 'href': href }
    ```
    3. Запускаем краулер — ура, ссылки собрались!
5. Теперь вместо того, чтобы просто выводить адреса страниц, попробуем собирать переходить на них.
    1. Аккуратно, ссылки относительные (`/centers/prices/21.html`), и скрепи не знает, как по ним ходить — нужно приделать к ним адрес сайта.
    2. Импортируем `import urllib.parse` в начале спайдера — эта библиотека соединяет куски адресов.
    3. Делаем адрес абсолютным: `abs_url = urllib.parse.urljoin('https://www.europegym.ru/', href)`
    5. Пишем в классе затычку-метод `parse_center`, пусть он просто делает `yield {}` для начала.
    4. Наконец, переходим по ссылке! Похоже на вывод данных, но вызываем со скрепи-запросом: `yield scrapy.Request(url=abs_url, callback=self.parse_center)`
6. Наконец, собираем сами данные. *Все* прайс-листы находятся в таблицах внутри `.hold-price`, и перед каждым стоит заголовок `h2`. Мы хотим получить только цены на персональные тренировки, то есть следующую таблицу после заголовка «Персональные тренировки».
    11. CSS не умеет фильтровать по тексту, значит, нам нужен xpath
    12. Выбираем все строки нужной таблицы: `rows = response.xpath('//h2[contains(text(), "Персональные тренировки")]/following-sibling::table[1]/tr')`
        * Подходящий заголовок: `//h2[contains(text(), "Персональные тренировки")]`
        * *Все* элементы после заголовка: `/following-sibling`
        * Только таблицы: `::table`
        * Только первая таблица: `[1]`
        * Наконец, все строки нужной таблицы: `/tr`.
    12. Пробуем достать текст из ячеек и переложить его в массив: `res = [[td.css(::text).extract_first().strip() for td in row.xpath('td')] for row in rows]`
    13. О нет! Текст некоторых ячеек обёрнут в `div`, а `::text` возвращает только текст из самого элемента.
    14. Напишем умную функцию `cell_text`, которая решит эту проблему:
    ```
    def cell_text(td):
          sel = 'div::text' if len(td.css('div')) else '::text'
          return td.css(sel).extract_first().strip()
    ```
    И перепишем разбор строки на `res = [[cell_text(td) for td in row.xpath('td')] for row in rows]`
    14. Ура! Теперь выплюнем данные из таблицы вместе с названием клуба: `yield { 'title': response.css('h1::text').extract_first(), 'table': res }`
1. Наконец, сложим данные в файл: `scrapy crawl pricelist -o data.json`.
2. По умолчанию скрепи записывает в файл бникод в виде  `\uXXXX`. Если мы хотим настоящий юникод, добавим в `settings.py`
```
FEED_EXPORT_INDENT = 2
FEED_EXPORT_ENCODING = "utf-8"
```
111. Готово, мы хакиры.
