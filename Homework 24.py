import pytest
import requests

# Владимир, добрый день! Сделал последний тест по вашему примеру. Сам сделал все тесты, кроме пятого. Изначально в
# weather_request не использовал переменную city_name, а просто написал Москва в поле q. Наверное, поэтому не получалось
# сделать 5 тест


def weather_request(city_name):
    """Получение данных о погоде по городу с сайта"""
    api_key = "358b79968edc92b3ae7789b368aa32de"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'lang': 'ru',
        'units': 'metric',
        'appid': api_key
    }

    response = requests.get(base_url, params=params)
    return response.json()


cities = [
    ('Москва', {"lon": 37.6156, "lat": 55.7522}),
    ('Воронеж', {"lon": 39.17, "lat": 51.6664}),
    ('Санкт-Петербург', {"lon": 30.2642, "lat": 59.8944}),
    ('Краснодар', {"lon": 38.9769, "lat": 45.0328}),
    ('Сочи', {"lon": 39.7303, "lat": 43.6}),
]


@pytest.fixture(scope='module')
def get_weather():
    """Фикстура для создания экземпляра"""
    return weather_request('Москва')


def test_weather_request_city_name(get_weather):
    """Проверяет, что в ответе API для Москвы поле name соответствует ожидаемому (Москва)"""
    assert get_weather['name'] == 'Москва'


def test_weather_request_coord(get_weather):
    """Проверяет, что координаты (longitude и latitude) в ответе API для Москвы соответствуют ожидаемым."""
    assert get_weather['coord'] == {'lon': 37.6156, 'lat': 55.7522}


def test_weather_request_weather_key(get_weather):
    """Проверяет, что в секции weather ответа API присутствуют ключи id, main, description, icon."""
    assert 'id' in get_weather['weather'][0]
    assert 'main' in get_weather['weather'][0]
    assert 'description' in get_weather['weather'][0]
    assert 'icon' in get_weather['weather'][0]


def test_weather_request_main_key(get_weather):
    """Проверяет, что в секции main ответа API присутствуют ключи для температуры, ощущаемой
    температуры, минимальной и максимальной температуры, давления и влажности."""
    assert 'temp' in get_weather['main']
    assert 'feels_like' in get_weather['main']
    assert 'temp_min' in get_weather['main']
    assert 'temp_max' in get_weather['main']
    assert 'pressure' in get_weather['main']
    assert 'humidity' in get_weather['main']


@pytest.mark.slow
@pytest.mark.parametrize('city_name, expected_coords', cities)
def test_weather_request_coord_parametrize_slow(city_name, expected_coords):
    """Проверяет, что для разных городов (параметризовано списком cities ) имя и координаты в ответе API
    соответствуют ожидаемым."""
    response = weather_request(city_name)
    assert response['coord'] == expected_coords

