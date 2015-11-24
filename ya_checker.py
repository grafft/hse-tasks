# coding=utf-8
import requests
import lxml.html
import re
import urllib
from lxml.cssselect import CSSSelector

# contest_id = 1671  # Seminar 9
# contest_id = 1786 # Seminar 10
contest_id = 1864  # Seminar 11

params = ['contestId=' + str(contest_id),
          'filter0=verdict%3DAC', 'filter1=userGroupName%3Dhse-minor-15-8',
          'filtersCount=2']
base_url = 'https://contest.yandex.ru/admin/contest-submissions'
rejudge_base_url = 'https://contest.yandex.ru/admin/contest-submissions/change-verdict'

url = '?'.join([base_url, '&'.join(params)])

cookies_dict = {
    'Session_id': '3:1448304062.5.0.1444554362822:CnStbQ:50.0|102246374.0.2|137381.881008.B0DTtfGaTdnDEtjBAma5sdRk35U',
}

sel_tr = CSSSelector('table[data-contest-id="{0}"] tr'.format(contest_id))

r = requests.get(url, cookies=cookies_dict)

m = re.search(r'window.csrfToken = \'(\S+)\';', r.text)
csrfToken = urllib.parse.quote_plus(m.group(1))

tree = lxml.html.fromstring(r.text)
results = sel_tr(tree)
while len(results) > 1:
    print('=' * 5 + 'Start next page' + '=' * 5)
    for i, node in enumerate(results[1:]):
        tr = lxml.html.fromstring(lxml.html.tostring(node))
        run_id = tr.attrib['data-run-id']

        judge_url = '?'.join([rejudge_base_url,
                              '&'.join([params[0], 'runId=' + run_id, 'verdict=ok',
                                        'csrf-token=' + csrfToken])])
        print('{0}: rejudge {1}'.format(i + 1, run_id))

        r1 = requests.post(judge_url, cookies=cookies_dict)
        judge_response = r1.json()

        if judge_response:
            print(judge_response.message)
        else:
            print('OK')

    r = requests.get(url, cookies=cookies_dict)
    tree = lxml.html.fromstring(r.text)
    results = sel_tr(tree)
else:
    print('There is no AC tasks')
