from cities import cities_list
from pprint import pprint
# Создаем пустое множество
city_game = set()
# Создаем плохие буквы, на которые города не должны заканчиваться
bad_letter = {"ь", "ъ", "ы", "ц", "й"}

# Проходим циклом по cities_list и забираем оттуда название городов
for key in cities_list:
    city = key['name']
    city_game.add(city)
# Преобразуем множество в список
city_list = list(city_game)
# Проходим циклом по списку и удаляем из множества города с окончанием на плохие буквы
for item in city_list:
    if item[-1] in bad_letter:
        city_game.remove(item)
# Запускаем цикл
while True:
    user_input = input('Введите название города: ')
    # Задаем условие, что при слове "стоп" цикл останавливается
    if user_input.lower() == 'стоп':
        print('Вы проиграли')
        break
    # Проверяем наличие пользовательского ввода в списке городов
    if user_input.capitalize() in city_game:
        # Убиреам введенный город
        city_game.remove(user_input.capitalize())
    # Проходим циклом по списку городов для ответа компьютера
        for i in city_game:
        # Находим совпадение последней буквы введенного города и первой буквы города из цикла
            if i[0] == user_input.upper()[-1]:
                # Выводим название города
                print(i)
            # Удаляем город из множества
                city_game.remove(i)
            # Прерываем цикл
                break
    # Если пользовательский ввода нет в списке городов, выводим проигрыш
    else:
        print('Вы проиграли')
        break

