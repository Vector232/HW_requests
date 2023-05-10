"""Нужно определить кто самый умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos."""
import requests


def SortForPowerstats(powerstats_name: str, hero_name_list: list):

    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'
    hero_list = requests.get(f'{url}/all.json').json()

    sorted_hero_list = sorted([hero for hero in hero_list if hero['name'] in hero_name_list], key=lambda x: x['powerstats'][powerstats_name], reverse=True)

    HeroTopList = {powerstats_name: {hero['name']: hero['powerstats'][powerstats_name] for hero in sorted_hero_list}}

    return HeroTopList


print(SortForPowerstats('intelligence', ['Hulk', 'Captain America', 'Thanos']))