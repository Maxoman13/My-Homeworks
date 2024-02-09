spec = '.,!?- '  # Спецсимволы для поиска в многострочных словах


class PalindromeStrategy:
    """
    Класс для определения стратегий
    """

    def is_palindrome(self, word: str) -> bool:
        """
        Метод для проверки палиндромов
        :param word: строка для проверки
        :return:
        """
        raise NotImplementedError


class SingleWordPalindrome(PalindromeStrategy):
    """
    Класс для проверки однострочных палиндромов
    """
    def is_palindrome(self, word: str) -> bool:
        """
        Метод для проверки однострочного палиндрома
        :param word:
        :return:
        """
        if word.lower() == word.lower()[::-1]:
            return True
        else:
            return False


class MultiWordPalindrome(PalindromeStrategy):
    """
    Класс для проверки многострочных палиндромов
    """
    def is_palindrome(self, word: str) -> bool:
        """
        Метод для проверки многострочного палиндрома
        :param word:
        :return:
        """

        for i in spec:
            word = word.replace(i, '')

        if word.lower() == word.lower()[::-1]:
            return True
        else:
            return False


class PalindromeContext:
    """
    Класс для объедеинения проверок палиндрома
    """
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy: PalindromeStrategy):
        """
        Метод для установки стратегии
        :param strategy:
        :return:
        """
        self.strategy = strategy

    def execute_strategy(self, word):
        """
        Метод для проверки палиндрома
        :param word: строка для проверки
        :return:
        """
        return self.strategy.is_palindrome(word)


class PalindromeFacade:
    """
    Класс для проверки палиндромов
    """
    def __init__(self):
        self.context = PalindromeContext()

    def check_palindrome(self, word: str) -> bool:
        """
        Метод для проверки палиндрома
        :param word: строка для проверки
        :return:
        """
        for i in spec:
            if i in word:
                self.context.set_strategy(MultiWordPalindrome())
            else:
                self.context.set_strategy(SingleWordPalindrome())
        return self.context.execute_strategy(word)


def main():
    """
    Функция для работы программы
    """
    facade = PalindromeFacade()
    while True:
        text = input('Введите слово или фразу для проверки: ')
        if not text:
            break
        print(f'"{text}" - палиндром: {facade.check_palindrome(text)}')


if __name__ == '__main__':
    main()