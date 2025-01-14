import copy
import csv
from pathlib import Path

from settings import ITEMS, ENCODING
from src.exeptions import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self._name = name[:10]
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @staticmethod
    def string_to_number(number: str):
        """
        Конвертирование строки в числа.
        """
        if number.replace('.', '').isdigit():
            if '.' in number:
                return float(number)
            else:
                return int(number)

    @classmethod
    def instantiate_from_csv(cls, file=ITEMS) -> None:
        """
        Инициализирует товары из csv файла.
        """
        cls.all = []
        # Проверка на наличие файла
        if not Path(file).exists():
            raise FileNotFoundError('Отсутствует файл item.csv')

        csv_dict = list()
        with open(file, 'r', encoding=ENCODING) as f:
            items: csv.DictReader = csv.DictReader(f)
            csv_dict = list(items)

        # Проверка на целостность файла
        if (csv_dict[0].get('name') and csv_dict[0].get('price') and csv_dict[0].get('quantity')) is None:
            raise InstantiateCSVError

        # Инициализация экземпляров из файла
        [cls(i['name'], cls.string_to_number(i['price']), cls.string_to_number(i['quantity'])) for i in csv_dict]

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Устанавливает название товара
        длиной не более 10 символов.

        :param name: Название товара.
        """
        self._name = name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def __add__(self, other) -> int:
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    def __repr__(self):
        """
        Выводит информацию о экземпляре независимо от подкласса
        """
        return f"{self.__class__.__name__}{tuple(self.__dict__.values())}"

    def __str__(self):
        return self._name

