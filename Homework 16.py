import csv
import json
from typing import List, Any, Dict

# Владимир, добрый день! Сделал два класа: TXT сам без вашего разбора(вроде бы все работало),
# с JSON помогло решение с TypeError, пытался сделать CSV по такому же принципу и завис. Ваш разбор помог.


class JsonAppendError(Exception):
    pass


class CsvFileHandler:
    """
    Класс CsvFileHandler
read_file(filepath, as_dict=False): Метод для чтения данных из CSV файла. По умолчанию данные должны возвращаться в виде списка списков, но при установке флага as_dict в True, данные должны возвращаться в виде списка словарей.
write_file(filepath, data, as_dict=False): Метод для записи данных в CSV файл. По умолчанию метод должен записывать данные в виде списка списков, но при установке флага as_dict в True, данные должны записываться в виде списка словарей.
append_file(filepath, data, as_dict=False): Метод для дописывания данных в CSV файл. Флаг as_dict работает аналогично как в методе write_file.
    """

    def __init__(self, filepath: str):
        self.data = None
        self.filepath = filepath

    def read_file(self, as_dict=False) -> List[Dict] | List[List]:
        """
        Метод для чтения данных из CSV файла.
        По умолчанию данные должны возвращаться в виде списка списков, но при установке флага as_dict в True, данные должны возвращаться в виде списка словарей.
        Должен быть реализован как метод экземпляра.
        :return: List[Dict] | List[List]
        """
        with open(self.filepath, 'r', encoding='windows-1251') as file:
            self.data = file.readlines()
            if as_dict:
                return [dict(zip(self.data[0].split(';'), line.split(';'))) for line in
                        self.data[1:]]
            else:
                return [line.split(';') for line in self.data]

    def write_file(self, data: List[Dict] | List[List], as_dict=False) -> None:
        """
        Метод для записи данных в CSV файл.
        По умолчанию метод должен записывать данные в виде списка списков, но при установке флага as_dict в True, данные должны записываться в виде списка словарей.
        Должен быть реализован как метод экземпляра.
        :param as_dict: bool
        :param data: List[Dict] | List[List]
        """
        with open(self.filepath, 'w', encoding='windows-1251') as file:
            if as_dict:
                file.writelines([';'.join(data[0].keys()) + '\n'])
                for line in data:
                    file.writelines([';'.join(line.values()) + '\n'])
            else:
                for line in data:
                    file.writelines([';'.join(line) + '\n'])

    def append_file(self, data: List[Dict] | List[List], as_dict=False) -> None:
        """
        Метод для дописывания данных в CSV файл.
        Флаг as_dict работает аналогично как в методе write_file.
        Должен быть реализован как метод экземпляра.
        :param as_dict: bool
        :param data: List[Dict] | List[List]
        """
        with open(self.filepath, 'a', encoding='windows-1251') as file:
            if as_dict:
                for line in data:
                    file.writelines([';'.join(line.values()) + '\n'])
            else:
                for line in data:
                    file.writelines([';'.join(line) + '\n'])


class JsonFileHandler:

    @staticmethod
    def read_file(filepath: str, as_dict=False) -> List[Dict] | List[List]:
        """
        Метод для чтения данных из JSON файла.
        Флаг as_dict работает аналогично как в классе CsvFileHandler.
        Должен быть реализован как метод экземпляра.
        :param as_dict: bool
        :param filepath: str
        :return: List[Dict] | List[List]
        """
        with open(f'{filepath}', 'r', encoding='UTF-8', newline='') as f:
            file = json.load(f)
            return file

    @staticmethod
    def write_file(filepath: str, data: List[Dict] | List[List], as_dict=False) -> None:
        """
        Метод для чтения данных из JSON файла.
        Флаг as_dict работает аналогично как в классе CsvFileHandler.
        Должен быть реализован как метод экземпляра.
        :param filepath: str
        :param as_dict: bool
        :param data: List[Dict] | List[List]
        """
        with open(f'{filepath}', 'w', encoding='UTF-8', newline='') as f:
            if as_dict:
                json.dump(dict(data), f, ensure_ascii=False, indent=4)
            else:
                json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def append_file(data: Any) -> None:
        """
        Метод для дописывания данных в JSON файл.
        При попытке вызова этого метода возникает исключение TypeError
        с сообщением, что данный тип файла не поддерживает операцию дописывания.
        Должен быть реализован как метод экземпляра.
        :param data: List[str]
        """
        raise JsonAppendError('Данный тип файла не поддерживает операцию дописывания')


class TxtFileHandler:
    """
        Класс для TXT файлов. Чтение, запись, дописывание.
        Работает со списком строк.
    """
    @staticmethod
    def read_file(filepath: str) -> List[str]:
        """
        Метод для чтение TXT файлов
        Принимает путь к файлу, отдает список строк
        :param filepath: str
        :return: List[str]
        """
        with open(f'{filepath}', 'r', encoding='UTF-8') as f:
            file = f.readlines()
            return file

    @staticmethod
    def write_file(filepath: str, data: List[str]) -> None:
        """
        Метод для записи или создания TXT файла
        Принимает список строк
        :param filepath: str
        :param data: List[str]
        """
        with open(f'{filepath}', 'w', encoding='UTF-8') as f:
            f.writelines(data)

    @staticmethod
    def append_file(filepath: str, data: List[str]) -> None:
        """
        Метод для дозаписи в TXT файл
        Принимает список строк
        :param filepath: str
        :param data: str
        """
        with open(f'{filepath}', 'a', encoding='UTF-8') as f:
            f.writelines(data)
