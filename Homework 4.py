phone_number = input("Введите номер телефона: ")
number = (phone_number.strip().strip('+').replace('(', '').replace(')', '').
          replace('-', '').replace(' ', ''))  # Находим и меняем скобки, пробелы, тире
if number.isdigit(): # Проверяем цифры из строки на длину
    if len(number) == 11:
        print(f'Номер телефона {phone_number} введен верно')
    else:
        print('Номер телефона должен быть длиннее')
else:
    print(f'Номер телефона {phone_number} должен состоять из цифр')


password = input("Введите ваш пароль: ")
if len(password) >= 8: # Проверяем длину пароля
    if not (password.islower() or password.isupper()): # Проверяем регистры
        special = '!'
        if special in password: # Проверяем спецсимволы
            space = ' '
            if space in password: # Проверяем пробел
                print('Пароль должен быть без пробела')
            else:
                print('Пароль подходит')
        else:
            print('Нужен восклицательный знак')
    else:
        print('В пароле должны быть символы всех регистров')
else:
    print('Пароль должен быть длинее')
