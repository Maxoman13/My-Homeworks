from cities import cities_list
import json

# Записываем и получаем json
# city_game = set()
# bad_letter = {"ь", "ъ", "ы", "ц", "й"}
#
# for city in cities_list:
#     if city['name'][-1].lower() not in bad_letter:
#         city_game.add(city['name'])
#
# city_list = list(city_game)
#
# with open('city_list', 'w', encoding='UTF-8') as file:
#     json.dump(city_list, file, ensure_ascii=False, indent=4)

# Открываем json для работы
with open('city_list', 'r', encoding='UTF-8') as file:
    json_data = json.load(file)

computer_city = None

while json_data:
    user_input = input('Введите название города: ')

    if user_input.lower() == 'стоп':
        print('Вы проиграли')
        break

    if user_input.capitalize() not in json_data:
        print('Такого города нет. Вы проиграли')
        break

    if user_input.capitalize() in json_data:
        json_data.remove(user_input.capitalize())
        print(f'Вы ввели: {user_input}')

    if computer_city:
        if computer_city[-1].lower() != user_input[0].lower():
            print('Вы проиграли')
            break

    for i in json_data:
        if i[0].lower() == user_input.lower()[-1]:
            computer_city = i

    json_data.remove(computer_city)

    print(f'Машина ввела: {computer_city}')
