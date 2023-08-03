class MixinLang:
    def __init__(self) -> None:
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        match self.__language:
            case 'EN':
                self.__language = 'RU'
            case 'RU':
                self.__language = 'EN'
        return self
