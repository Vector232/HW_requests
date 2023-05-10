'''Нужно написать программу, которая выводит все вопросы за последние два дня и содержит тэг "Python".'''

import requests
import datetime

def allQuestionsWithЕheTag(tag):
    now = int(datetime.datetime.utcnow().timestamp())

    url = 'https://api.stackexchange.com/2.3'
    res = requests.get(f'{url}/questions?fromdate={now - 172800}&todate={now}&order=desc&tagged=Python&sort=activity&site=stackoverflow').json()
    sorted_res_list = sorted(res['items'], key=lambda x: x['creation_date'], reverse=True)

    return sorted_res_list


ans = allQuestionsWithЕheTag('Python')

for qestion in ans:
    print(datetime.datetime.fromtimestamp(qestion['creation_date']), qestion['tags'])
    