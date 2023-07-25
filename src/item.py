import csv

from settings import ITEMS, ENCODING


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
        self._name = name[:10]
        self.price = float(price)
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
    def instantiate_from_csv(cls):
        """
        Инициализирует товары из csv файла.
        """
        with open(ITEMS, 'r', encoding=ENCODING) as f:
            items: csv.DictReader = csv.DictReader(f)
            [cls(i['name'], cls.string_to_number(i['price']), cls.string_to_number(i['quantity'])) for i in items]

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
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self._name}', {int(self.price)}, {self.quantity})"

    def __str__(self):
        return self._name
