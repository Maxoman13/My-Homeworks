from dataclasses import dataclass
from pprint import pprint

import requests
from marshmallow import Schema, fields, ValidationError, validate, INCLUDE, post_load
from marshmallow_jsonschema import JSONSchema

# Владимир, здравствуйте! Сделал всё через вложенные схемы. Сначала описал все данные, потом понял, что это перебор)
# Немного не понял, что должны получить в итоге, потому что у меня получался такой же JSON, как при получение с сайта.
# После вашего разбора понял, что должно быть в итоге.


def get_weather(city_name):
    """Получение данных о погоде по городу с сайта"""
    api_key = ""
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'lang': 'ru',
        'units': 'metric',
        'appid': api_key
    }

    response = requests.get(base_url, params=params)
    return response.json()


@dataclass
class CurrentWeather:
    """Датакласс с данными о погоде в городе"""
    name: str
    country: str
    temp: float
    feels_like: float
    humidity: int
    pressure: int
    description: str
    wind_speed: float

    def __str__(self):
        """Информация о городе в читаемом виде"""
        return f'В {self.name}, {self.country}\n'\
               f'Температура {self.temp}. Ощущается как {self.feels_like}\n'\
               f'Влажность {self.humidity}. Давление {self.pressure}.\n'\
               f'Скорость ветра {self.wind_speed}.\n'\
               f'Описание погоды {self.description}'


class MainSchema(Schema):
    """Схема для валидации данных по ключу Main"""
    feels_like = fields.Float(required=True)
    humidity = fields.Int(required=True)
    pressure = fields.Int(required=True)
    temp = fields.Float(required=True, validate=validate.Range(min=-50, max=50))

    class Meta:
        """unknown = INCLUDE указывает, что в полученных данных есть другие поля, которых нет в схеме"""
        unknown = INCLUDE


class SysSchema(Schema):
    """Схема для валидации данных по ключу Sys"""
    country = fields.Str(required=True)

    class Meta:
        """unknown = INCLUDE указывает, что в полученных данных есть другие поля, которых нет в схеме"""
        unknown = INCLUDE


class DescriptionSchema(Schema):
    """Схема для валидации данных по ключу Description"""
    description = fields.Str(required=True)

    class Meta:
        """unknown = INCLUDE указывает, что в полученных данных есть другие поля, которых нет в схеме"""
        unknown = INCLUDE


class WindSchema(Schema):
    """Схема для валидации данных по ключу Wind"""
    speed = fields.Float(required=True)

    class Meta:
        """unknown = INCLUDE указывает, что в полученных данных есть другие поля, которых нет в схеме"""
        unknown = INCLUDE


class CurrentWeatherSchema(Schema):
    """Основная схема для валидации данных. Принимает в себя другие схемы как вложенные"""
    main = fields.Nested(MainSchema)
    name = fields.Str(required=True)
    sys = fields.Nested(SysSchema)
    weather = fields.List(fields.Nested(DescriptionSchema))
    wind = fields.Nested(WindSchema)

    class Meta:
        """unknown = INCLUDE указывает, что в полученных данных есть другие поля, которых нет в схеме"""
        unknown = INCLUDE

    @post_load
    def make_current_weather(self, data, **kwargs) -> CurrentWeather:
        """
        Создание экземпляра класса CurrentWeather из словаря
        Используется после валидации данных
        """

        return CurrentWeather(
            name=data['name'],
            country=data['sys']['country'],
            temp=data['main']['temp'],
            feels_like=data['main']['feels_like'],
            humidity=data['main']['humidity'],
            pressure=data['main']['pressure'],
            description=data['weather'][0]['description'],
            wind_speed=data['wind']['speed'],
        )


def main():
    #  Получаем город от пользователя
    city_name = input('Введите название города: ')
    #  Получаем город с сайта
    weather_data = get_weather(city_name)
    #  Схема для данных
    current_weather_schema = CurrentWeatherSchema()
    #  Сохранение JSON схемы
    json_schema = JSONSchema().dump(current_weather_schema)

    pprint(json_schema)

    try:
        #  Десериализация и валидация полученных данных. При ошибке будет выведено сообщение.
        validate_data = current_weather_schema.load(weather_data)
        print(validate_data)
    except ValidationError as e:
        print(e.messages)


if __name__ == '__main__':
    main()
