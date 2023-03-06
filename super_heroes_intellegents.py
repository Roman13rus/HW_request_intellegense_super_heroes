import requests
import json


def get_information_super_heroes(route):    # Функция для загрузки данных о всех супергероях
     url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'
     response = requests.get(f'{url}{route}.json')
     heroes_data = response.json()
     return heroes_data

def finding_intelligence_superheroes(list_heroes):   # функция определения самого умного супергероя(из списка принимаемого на вход) 
    best_intelligence = 0
    name = ''
    data = get_information_super_heroes('/all') # запрос jsonфайла из api сайта
    for hero in data:
        if hero["name"] in list_heroes:
            if hero["powerstats"]["intelligence"] > best_intelligence:
                best_intelligence = hero["powerstats"]["intelligence"]
                name = hero["name"]
    return (f'Самый умный супергерой: {name}, его показатель равен {best_intelligence}.')
print(finding_intelligence_superheroes(['Hulk','Captain America', 'Thanos']))


