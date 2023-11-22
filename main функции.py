import json


def get_city_from_json(file_name: str = 'cities.json') -> set:
    """
        Принимает json файл
        :param file_name: 'cities.json'
        :return: Сет городов
    """
    with open(file_name, 'r', encoding='UTF-8') as file:
        cities_set = set(json.load(file))

    return cities_set


bad_letter = {"ь", "ъ", "ы", "й", "ё"}


def check_main_game_rule(last_round_city: str, current_round_city: str) -> bool:
    """
    Функция принимает два города и проверяет, что первая буква города current_round_city
    равна последней букве города last_round_city, также проверяем на плохие буквы в конце last_round_city,
    если попадаем в плохие буквы, то используем предпоследнюю букву
    :param last_round_city: Город из прошлого раунда
    :param current_round_city: Город из текущего раунда
    :return: bool
    """
    if last_round_city[-1].lower() == current_round_city[0].lower():
        return True
    elif last_round_city[-1].lower() in bad_letter:
        if current_round_city[0].lower() == last_round_city[-2].lower():
            return True
        else:
            return False
    else:
        return False


def computer_move(cities_set: set, last_round_city: str) -> str | None:
    """
    Функция принимает сет городов, город из прошлого раунда. Проходит циклом по сету
    городов, проверяя каждый город на главное правило игры
    :param cities_set:
    :param last_round_city:
    :return:
    """
    for city in cities_set:
        if check_main_game_rule(last_round_city, city):
            return city
    else:
        return None


def main():
    # Читаем json файл с городами и получаем сет городов
    cities_set = get_city_from_json()

    # Объявляем переменную под город компьютера
    computer_city = None

    while cities_set:
        # Ввод города человеком
        human_city = input('Введите город: ')

        # Проверка на стоп
        if human_city == 'стоп':
            print('Вы проиграли')
            break

        # Проверка на вхождение в сет
        if human_city not in cities_set:
            print('Вы проиграли. Такого города нет')
            break

        # Если компьютер уже ходил. Делаем проверку на последнюю букву
        if computer_city:
            if not check_main_game_rule(computer_city, human_city):
                print('Вы проиграли')
                break

        # Удаление из сета
        cities_set.remove(human_city)

        # Принт ход человека
        print(f'Вы ввели: {human_city}')

        # Ход компьютера
        computer_city = computer_move(cities_set, human_city)

        if not computer_city:
            print('Вы выиграли')
            break

        # Удаление из сета
        cities_set.remove(computer_city)
        # Принт ход компьютера
        print(f'Машина ввела: {computer_city}')

    else:
        print('Компьютер проиграл. Вы выиграли!')


main()
