from src.item import Item
from src.mixins import MixinLang


class Keyboard(Item, MixinLang):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        """
        Создание экземпляра класса item.

        :param name: Название товара (в отличии от родительского класса Item, не имеет ограничения по длине имени)
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name

    @property
    def name(self):
        """Геттер name, нужен для переопределения name в Item"""
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Устанавливает название товара,
        в отличии от родительского класса Item,
        без ограничения по длине имени

        :param name: Название товара.
        """
        self._name = name

