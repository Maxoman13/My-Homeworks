from marvel import full_dict
from pprint import pprint
from typing import List, Dict, Any

# Задание 1 Получаем данные от пользователя и разделяем ее по пробелам

numbers: List[str] = input('Введите цифры через пробел: ').split(' ')

# Проверяем элементы на число

int_numbers: List[int | None] = list(map(lambda num: int(num) if num.isdigit() else None, numbers))

# Для каждого числа, введенного пользователем, получаем фильм

result_films: dict = dict(filter(lambda movie: movie[0] in int_numbers, full_dict.items()))

pprint(result_films)

# Задание 2 Собираем множество по значению director

director_set: set = {movie[1]['director'] for movie in full_dict.items()}

pprint(director_set)

# Задание 3 Делаем строку в year

year_str: Dict[int, Dict[str, str]] = \
    {key: {k: str(v) if k == 'year' else v for k, v in value.items()} for key, value in full_dict.items()}

pprint(year_str)

# Задание 4 Фильтруем фильмы, которые начинаются на Ч

result_film_word: Dict[int, Dict[str, Any]] = (
    dict(filter(lambda movie: movie[1]['title'].startswith('Ч'), full_dict.items())))

pprint(result_film_word)

# Задание 5 Сортировка по director

sort_full_dict: Dict[int, Dict[str, Any]] = (
     dict(sorted(full_dict.items(), key=lambda movie: movie[1]['director'])))

pprint(sort_full_dict, sort_dicts=False)

# Задание 6 Сортировка по director и stage

sort_full_dict2: Dict[int, Dict[str, str | int]] = (
    dict(sorted(full_dict.items(), key=lambda movie: (movie[1]['stage'], movie[1]['director']))))

pprint(sort_full_dict2, sort_dicts=False)

# Задание 7 Сортировка по stage и фильтр по букве Ж.

result_film3: Dict[int, Dict[str, str]] = (
    dict(sorted(filter(lambda movie: movie[1]['title'].startswith('Ж'), full_dict.items()),
                key=lambda movie: (movie[1]['stage']))))

pprint(result_film3, sort_dicts=False)

# Владимир, добрый день! Пытлася сделать mypy по разбору, все равно не прохожу проверку. Буду разбираться, пока сдаю так.