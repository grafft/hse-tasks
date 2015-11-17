# coding=utf-8
import requests
import lxml.html
from lxml.cssselect import CSSSelector


#statement_id = '8483' #seimanar 2
#statement_id = '8459' #seimanar 3
#statement_id = '8545' #seimanar 4
#statement_id = '8634' #seimanar 5
#statement_id = '8794' #seimanar 6
statement_id = '8928' #seimanar 7
params = ['problem_id=0', 'group_id=3618', 'user_id=0', 'lang_id=-1', 'status_id=-1',
          'statement_id='+statement_id, 'objectName=submits', 'count=500', 'with_comment=',
          'page=0', 'action=getHTMLTable']
base_url = 'http://informatics.mccme.ru/moodle/ajax/ajax.php'
url = '?'.join([base_url, '&'.join(params)])

r = requests.get(url)
response = r.json()
result_table = response['result']['text']
tree = lxml.html.fromstring(result_table)

sel_tr = CSSSelector('table tr')
results = sel_tr(tree)
for node in results[1:]:
    tr = lxml.html.fromstring(lxml.html.tostring(node))
    sel_id = CSSSelector('td:first-child')
    sel_status = CSSSelector('td:first-child' + '+td' * 5)
    run_id = sel_id(tr)
    status = sel_status(tr)
    status_str = lxml.html.tostring(status[0])
    id_str = lxml.html.tostring(run_id[0])
    if 'OK\n' == status[0].text:
        info = run_id[0].text.split('-')
        judge_url = '/'.join(['http://informatics.mccme.ru/py/run/rejudge',
                              info[0], info[1], '8'])
        print(judge_url)

        cookies_dict = {'MoodleSession':'9naahjfu0954l4i1478qr185s7',
                        'MOODLEID_':'%25E2%25C5%250EM%25BDr%25A6',
                        'MoodleSessionTest':'vmpweoBttr'}

        r1 = requests.get(judge_url, cookies=cookies_dict)
        judge_response = r1.json()
        if judge_response['result'] == 'ok':
            print('OK')
        else:
            print(judge_response['message'])