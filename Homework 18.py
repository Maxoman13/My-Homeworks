import json
from typing import List, Dict, Set


class JsonFile:
    """
    Класс для работы с Json.
    read_file() - чтение
    write_file() - запись
    """
    def __init__(self, file_name: str):
        self.file_name = file_name

    def read_file(self):
        """
        Метод для чтения данных из JSON файла.
        :return: горорода из JSON файла.
        """
        with open(self.file_name, 'r', encoding='utf-8') as file:
            data_file = json.load(file)
        return data_file

    def write_file(self, data_file: str):
        """
        Метод для записи данных в JSON файла.
        :param data_file: данные для записи
        :return: None
        """
        with open("result.json", 'w', encoding='utf-8') as file:
            json.dump(data_file, file, ensure_ascii=False, indent=4)


class Cities:
    """
    Класс для получения данных о городах из JSON-файла.
    """
    def __init__(self, city_data):
        self.city_data = city_data
        self.names_set = self.__get_set()

    def __get_set(self):
        """
        Получение сета городов
        :return: сет городов
        """
        names_set = set()
        for city in self.city_data:
            names_set.add(city['name'])
        return names_set


class CityGame:
    """
    Класс для игры в города.
    """
    def __init__(self, cities: Cities):
        self.cities_obj = cities
        self.cities: Set[str] = self.cities_obj.names_set
        self.human_city: str = ''
        self.computer_city: str = ''

    @staticmethod
    def check_rule(last_round_city: str, current_round_city: str) -> bool:
        """
        Проверка правил игры
        :param last_round_city: Последний город, на последнюю букву которого, должен называться следующий город
        :param current_round_city: Текущий город, который должен называться на последнюю букву последнего города
        :return: True если правила соблюдены, иначе False
        """
        bad_letter = {"ь", "ъ", "ы", "й", "ё"}  # Сет плохих букв
        if last_round_city[-1].lower() == current_round_city[0].lower():
            return True
        # Если город заканчивается на плохую букву, сдвигаем на одну букву
        elif last_round_city[-1].lower() in bad_letter:
            if current_round_city[0].lower() == last_round_city[-2].lower():
                return True
            else:
                return False
        else:
            return False

    def human_turn(self):
        """
        Ход человека
        """
        self.human_city = input('Введите город: ')

        if self.human_city == 'стоп':
            print('Вы проиграли')
            return False

        if self.human_city not in self.cities:
            print(f'Города {self.human_city} нет в списке. Вы проиграли')
            return False

        if self.computer_city:
            if not self.check_rule(self.computer_city, self.human_city):
                print(f'Вы проиграли. Ваш ответ не начинается на букву {self.computer_city[-1]}')
                return False

        self.cities.remove(self.human_city)
        self.human_city = self.human_city
        return True

    def computer_turn(self):
        """
        Ход компьютера
        """
        for city in self.cities:
            if self.check_rule(self.human_city, city):
                print(f'Компьютер называет город: {city}')
                self.computer_city = city
                self.cities.remove(city)
                return True
        else:
            print("Человек победил")
            return False


class GameManager:
    """
    Класс управления игрой в города. Этот класс принимает экземпляры классов JsonFile , Cities и CityGame
    в качестве аргументов.
    """
    def __init__(self, json_file: JsonFile, cities: Cities, game: CityGame):
        self.json_file = json_file
        self.cities = cities
        self.game = game

    def __start_game(self):
        """
        Метод начала игры и добавления результата игры в JSON
        """
        while True:
            if not self.game.human_turn():
                json_file.write_file("Компьютер победил")
                break
            if not self.game.computer_turn():
                json_file.write_file("Человек победил")
                break

    def __call__(self):
        """
        Метод для запуска игры
        """
        self.__start_game()
        print('Игра окончена')


if __name__ == "__main__":
    # Создаем экземпляр класса JsonFile
    json_file = JsonFile("cities.json")
    # Создаем экземпляр класса Cities
    cities = Cities(json_file.read_file())
    # Создаем экземпляр класса CityGame
    game = CityGame(cities)
    # Создаем экземпляр класса GameManager
    game_manager = GameManager(json_file, cities, game)
    # Запускаем игру
    game_manager()
