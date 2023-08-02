class Node:
    def __init__(self, lang):
        self.lang = lang
        self.change_lang = None

    def __call__(self, *args, **kwargs):
        return self.lang


class MixinLang:
    def __init__(self) -> None:
        self.__language = None
        self.en = Node('EN')
        self.ru = Node('RU')
        self.en.change_lang = self.ru
        self.ru.change_lang = self.en

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        pass
        # match self.__language:
        #     case 'EN':
        #         self.__language = 'RU'
        #     case 'RU':
        #         self.__language = 'EN'


if __name__ == '__main__':
    m = MixinLang()
    m.change_lang()
