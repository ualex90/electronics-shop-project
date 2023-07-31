from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int = 1) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim
        self.__number_of_sim = self.number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number: int):
        error = 'Количество физических SIM-карт должно быть целым числом больше нуля.'
        if not isinstance(number, int):   # Если не целочисленное значение, вызовим исключение
            raise ValueError(error)
        elif number > 0:                  # Если число больше 0, запишем значение
            self.__number_of_sim = number
        else:                             # Иначе вызовим исключение
            raise ValueError(error)

