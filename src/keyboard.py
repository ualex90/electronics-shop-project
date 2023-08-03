from src.item import Item
from src.mixins import MixinLang


class Keyboard(Item, MixinLang):
    def __init__(self, name_: str, price: float, quantity: int):
        super().__init__(name_, price, quantity)
        """
        Создание экземпляра класса item. Имеет свойства Item, 
        дополнеными возможностью переключения языка клавиатуры из MixinLang

        :param name_: Название товара (в отличии от родительского класса Item, не имеет ограничения по длине имени)
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name_
