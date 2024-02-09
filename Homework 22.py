from abc import ABC, abstractmethod
from typing import List

"""
Владимир, добрый день. Немного задержал сдачу, запутался в классах и паттернах.
"""

#  Список размера пицц
pizza_size = ['Маленькая', 'маленькая', 'Средняя', 'средняя', 'Большая', 'большая']


class IngredientFactory(ABC):
    """
    Абстракный класс для создания ингридиентов пиццы
    """

    @abstractmethod
    def create_cheese(self):
        """
        Метод выбора сыра в пиццу
        """
        pass

    @abstractmethod
    def create_sauce(self):
        """
        Метод выбора соуса в пиццу
        """
        pass

    @abstractmethod
    def create_meat(self):
        """
        Метод выбора мяса в пиццу
        """
        pass

    @abstractmethod
    def create_vegetables(self):
        """
        Метод выбора овощей в пиццу
        """
        pass


class DodoIngredientFactory(IngredientFactory):
    """
    Конкретные ингредиенты для пиццы
    """
    def __init__(self, cheese_pizza, sauce_pizza, meat_pizza, vegetables_pizza):
        self.cheese = cheese_pizza
        self.sauce = sauce_pizza
        self.meat = meat_pizza
        self.vegetables = vegetables_pizza

    def create_cheese(self):
        return self.cheese.lower()

    def create_sauce(self):
        return self.sauce.lower()

    def create_meat(self):
        return self.meat.lower()

    def create_vegetables(self):
        return self.vegetables.lower()


class SizeFactory:
    """
    Фабрика для создания размеров пиццы
    """
    def __init__(self, size):
        self.size = size

    def create_size(self, size):
        self.size = size
        if self.size in pizza_size:
            return self.size.lower()
        else:
            return None


class PizzaBuilder:
    """
    Класс строителя: собирает пиццу, используя ингредиенты и размеры
    """
    def __init__(self, ingredient_factory, size_factory, pizza_type):
        self.ingredient_factory = ingredient_factory
        self.size_factory = size_factory
        self.pizza_type = pizza_type
        self.size = None

    def set_size(self, size):
        """
        Метод устанавливает размер пиццы
        :param size:
        :return:
        """
        self.size = self.size_factory.create_size(size)

    def build(self):
        """
        Метод сборки и описания пиццы
        :return:
        """
        cheese = self.ingredient_factory.create_cheese()
        sauce = self.ingredient_factory.create_sauce()
        meat = self.ingredient_factory.create_meat()
        vegetables = self.ingredient_factory.create_vegetables()
        return f'{self.size} пицца {self.pizza_type} с сыром {cheese}, {meat}, {vegetables}, соусом {sauce}'


def create_pizza():
    """
    Функция для создания пиццы
    :return:
    """
    cheese = input('Выберите сыр в пиццу ')  # Пользователь выбирает сыр для пиццы
    sauce = input('Выберите соус в пиццу ')  # Пользователь выбирает соус для пиццы
    meat = input('Выберите мясо в пиццу ')  # Пользователь выбирает мясо для пиццы
    vegetables = input('Выберите овощи в пиццу ')  # Пользователь выбирает овощи для пиццы
    size = input('Выберите размер пиццы(маленькая, средняя, большая) ')  # Пользователь выбирает размер пиццы
    ingredient_factory = DodoIngredientFactory(cheese, sauce, meat, vegetables)
    size_factory = SizeFactory(size)
    pizza_type = 'конструктор'

    builder = PizzaBuilder(ingredient_factory, size_factory, pizza_type)
    builder.set_size(size)
    return builder.build()


def main():
    """
    Основная функция для запуска создания заказа пиццы
    :return:
    """
    order = create_pizza()
    print(f'Ваш заказ {order}')


if __name__ == "__main__":
    main()