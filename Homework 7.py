user_input = input("Введите номер телефона: ")
num = (user_input.strip().replace('+', '').replace('(', '').replace(')', '').
       replace('-', '').replace(' ', ''))
print(num)
phone_number = num.split(';')
for number in phone_number:
    if not len(number) == 11:
        raise TypeError(f'Номер {number} должен содержать 11 символов')
    elif not number.isdigit():
        raise TypeError(f'Номер {number} должен состоять из цифр')
    elif not number.startswith(('8', '+7', '7')):
        raise TypeError(f'Номер {number} должен начинаться с +7 или 8')


data_lst = ['1', '2', '3', '4d', 5]
item_list = []

for item in data_lst:
    try:
        item_list.append(int(item))
        print(item_list)
    except ValueError:
        print(f"{item} не является числом")