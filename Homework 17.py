from abc import ABC, abstractmethod
from typing import Dict


class SmartHome(ABC):
    """ Метод для умных устройств """
    def __init__(self, name: str):
        """
        Инициализация умного устройства.

        :param name: название устройства
        """
        self.name = name

    @abstractmethod
    def switch_on(self):
        """ Включить устройство """
        pass

    @abstractmethod
    def switch_off(self):
        """ Выключить устройство """
        pass

    @abstractmethod
    def get_condition(self):
        """ Получить состояние """
        pass


class SmartLight(SmartHome):
    """
    Класс умной лампочки
    """
    def __init__(self, name: str):
        """
        Иницилизация умной лампочки
        :param name: Название устройства
        """
        super().__init__(name)
        self.bright = 0
        self.condition = False

    def switch_on(self):
        """
        Включить лампочку
        :return: None
        """
        self.condition = True

    def switch_off(self):
        """
        Выключить лампочку
        :return: None
        """
        self.condition = False

    def set_bright(self, bright: int):
        """
        Регулировать яркость лампочки.

        :param bright: уровень яркости
        """
        self.bright = bright

    def get_condition(self):
        """
        Получить текущее состояние лампочки.
        :return: состояние лампочки
        """
        if self.condition:
            return f'Свет включен. Уровень яркости {self.bright}'
        else:
            return f'Лампочка в {self.name} не работает, включите её'


class SmokeScreen(SmartHome):
    """
    Класс для датчика дыма
    """
    def __init__(self, name: str):
        """
        Иницилизация датчика дыма
        :param name: Название устройства
        """
        super().__init__(name)
        self.smoke_lvl = 0
        self.condition = False

    def switch_on(self):
        """
        Включить датчик
        :return: None
        """
        self.condition = True

    def switch_off(self):
        """
        Выключить датчик
        :return: None
        """
        self.condition = False

    def get_condition(self):
        """
        Получить состояние датчика.
        """
        if self.condition:
            return f'В {self.name} датчик дыма работает'
        else:
            return f'В {self.name} датчик дыма не работает'

    def smoke_check(self, smoke_lvl: int):
        """
        Проверка уровня задымления
        :param smoke_lvl: уровень дыма
        :return: True, если есть дым
        """
        self.smoke_lvl = smoke_lvl
        if self.smoke_lvl == 0:
            return False
        else:
            return True


class SmartWet(SmartHome):
    """
    Класс для увлажнителя
    """
    def __init__(self, name: str):
        """
        Иницилизация для увлажнителя
        :param name: Название устройства
        """
        super().__init__(name)
        self.wet = 0
        self.condition = False

    def switch_on(self):
        """
        Включить устройство
        :return: None
        """
        super().switch_on()
        self.condition = True

    def switch_off(self):
        """
        Выключить устройство
        :return: None
        """
        super().switch_off()
        self.condition = False

    def wet_lvl(self, wet_lvl: int):
        """
        Задаем уровень влажности
        :param wet_lvl: уровень влажности
        """
        self.wet = wet_lvl

    def get_condition(self):
        """
        Состояние увлажнителя
        """
        if self.condition:
            return f'Уровень влажности {self.wet}'
        else:
            return f'Уровень влажности в {self.name} не работает, включите его'


class AlertMixin:
    """
    Миксин для уведомлений
    """
    def send_message(self, message: str):
        """
        Отправить уведомление
        :param message: уведомление
        """
        print(f'Вам уведомление {message}')


class AddWifiMixin:
    """
    Миксин для подключения к Wi-fi
    """

    def wifi_connect(self, name_wifi: str, password: str):
        """
        Подклбчение к wi-fi
        :param name_wifi: название wi-fi
        :param password: пароль
        """
        if password == 'qwerty_123':
            print(f"Подключено к Wi-Fi сети {name_wifi}")
        else:
            print('Пароль неверный')


class TimeTableMixin:
    """
    Миксин для расписания работы
    """
    def __init__(self):
        self.worktime = {}

    def set_time(self, worktime: Dict[str, str]):
        self.worktime = worktime


class SmartLightYandex(SmartLight, AddWifiMixin):
    """
    Умная лампочка Yandex.
    """
    pass


class SmartSmokeDetector(SmokeScreen, AlertMixin):
    """
    Умный датчик дыма.
    """
    pass


class SmartWetYandex(SmartWet, TimeTableMixin):
    """
    Умный увлажнитель Yandex.
    """
    pass


# Симуляция работы умного дома
light = SmartLightYandex("Гостиная")
light.wifi_connect("Домашний Wi-Fi", "пароль123")
smoke_detector = SmartSmokeDetector("Кухня")
wet = SmartWetYandex("Спальня")
wet.set_time({"08:00": "включить", "23:00": "выключить"})


light.switch_on()  # Включить лампочку
light.set_bright(70)  # Установить яркость 70%
smoke_detector.switch_on()  # Включить датчик дыма
wet.switch_on()  # Включить увлажнитель
wet.wet_lvl(50)  # Установить уровень влажности 50%

print(light.get_condition())  # Получить состояние лампочки
print(smoke_detector.get_condition())  # Получить состояние датчика дыма
print(wet.get_condition())  # Получить состояние увлажнителя

if smoke_detector.smoke_check(10):  # Проверить наличие дыма
    smoke_detector.send_message("Обнаружен дым на кухне!")  # Отправить срочное уведомление
