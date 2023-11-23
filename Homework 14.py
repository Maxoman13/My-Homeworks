from typing import Callable
import csv

# Задание № 1

SPECIAL = '!@$#-_'  # Спецсимволы


# Декоратор с проверкой пароля
def password_checker(func: Callable) -> Callable:
    def checker(password: str) -> str:
        # Проверка длины
        if len(password) < 8:
            raise ValueError(f'Пароль должен быть не менее 8 символов')
        # Проверка на цифры
        elif not any(map(str.isdigit, password)):
            raise ValueError(f'Пароль должен содержать не менее 1 числа')
        # Проверка на буквы
        elif not any(map(str.isalpha, password)):
            raise ValueError(f'Пароль должен содержать не менее 1 буквенного символа')
        # Проверка на верхний регистр
        elif not any(map(str.isupper, password)):
            raise ValueError(f'Пароль должен содержать не менее 1 символа в верхнем регистре')
        # Проверка на нижний регистр
        elif not any(map(str.islower, password)):
            raise ValueError(f'Пароль должен содержать не менее 1 символа в нижнем регистре')
        # Проверка на спецсимволы
        elif not any(map(lambda x: x in SPECIAL, password)):
            raise ValueError(f'Пароль должен содержать не менее 1 специального символа')
        # Проверка на пробел
        elif ' ' in password:
            raise ValueError(f'Пароль содержит пробел')
        # Если прошли все проверки запускаем функцию
        else:
            return func(password)
    return checker


# Оборачиваем функцию декоратором.
@password_checker
def register_user(password: str) -> None:
    print(f"Вы зарегистрированы с паролем {password}")


register_user('Qwertyееее1!')


# Задание № 2

# Декоратор для проверки пароля пользователя
def password_validator(length: int = 8, uppercase: int = 1, lowercase: int = 1, special_chars: int = 1) -> Callable:
    """
    Декоратор для валидации паролей.
    Параметры:
    length (int): Минимальная длина пароля (по умолчанию 8).
    uppercase (int): Минимальное количество букв верхнего регистра (по умолчанию 1).
    lowercase (int): Минимальное количество букв нижнего регистра (по умолчанию 1).
    special_chars (int): Минимальное количество спец-знаков (по умолчанию 1).
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(username: str, password: str) -> None:
            if len(password) < length:
                raise ValueError(f'Пароль должен быть не менее {length} символов')
            elif not any(map(str.isupper, password)):
                raise ValueError(f'Пароль должен содержать не менее {uppercase} символа в верхнем регистре')
            elif not any(map(str.islower, password)):
                raise ValueError(f'Пароль должен содержать не менее {lowercase} символа в нижнем регистре')
            elif not any(map(lambda x: x in SPECIAL, password)):
                raise ValueError(f'Пароль должен содержать не менее {special_chars} специальных символов')
            elif ' ' in password:
                raise ValueError(f'Пароль содержит пробел')
            return func(username, password)

        return wrapper

    return decorator


# Декоратор для проверки имени пользователя
def username_validator(func: Callable) -> Callable:
    """
        Декоратор для  имени пользователя.
        :param func: функция для обертки
        :куегки: обернутая функция
        """
    def wrapper(username: str, password: str) -> None:
        if ' ' in username:
            raise ValueError(f'{username} содержит пробел')
        else:
            return func(username, password)
    return wrapper


# Оборачиваем функцию декоратором. Функция при правильных username и passwoed записывает их в файл
@password_validator()
@username_validator
def user_register(username: str, password: str) -> None:
    """
    Функция для регистрации нового пользователя и записи пользователя в файл.
    Параметры:
    username (str): Имя пользователя.
    password (str): Пароль пользователя.
    """
    with open('user.csv', 'a', encoding='windows-1251', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([username, password])


user_register('Maxoman13', 'Warior_13')
