'''Нужно написать программу, которая выводит все вопросы за последние два дня и содержит тэг "Python".'''

import requests
import datetime

def allQuestionsWithЕheTag(tag):
    now = int(datetime.datetime.utcnow().timestamp())

    url = 'https://api.stackexchange.com/2.3'
    res = requests.get(f'{url}/questions?order=desc&tagged=Python&site=stackoverflow').json()

    sorted_res_list = sorted([question for question in res['items'] if question['creation_date'] >= now - 172800], key=lambda x: x['creation_date'], reverse=True)

    return sorted_res_list


ans = allQuestionsWithЕheTag('Python')

for qestion in ans:
    print(datetime.datetime.fromtimestamp(qestion['creation_date']), qestion['tags'])
    