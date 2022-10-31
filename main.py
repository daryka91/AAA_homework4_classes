import json
import keyword


class ColourMixin:
    """окрашивает текст"""

    def __str__(self):
        repr_color_code = self.repr_color_code
        to_base_colour = self.to_base_colour
        repr_colour = '\033[' + f'{self.repr_color_code}' + 'm'
        to_base_colour = '\033[' + f'{self.to_base_colour}' + 'm'
        return f'{repr_colour}{self.title} | {self.price}{to_base_colour}'


class MapJson:
    """ преобразeует JSON-объеĸты в python-объеĸты с доступом ĸ атрибутам через точĸу"""

    def __init__(self, input_dict: dict):
        self.__data = {}
        for key, value in input_dict.items():  # Убедиться, что входящие данные можно преобразовать в словарь
            if keyword.iskeyword(key):  # Если некоторые атрибуты являются ключевыми словами Python
                key += "_"  # Затем добавим подчеркивание после
            self.__data[key] = value

    def __getattr__(self, item):
        value = self.__data.get(item)
        if isinstance(value, dict):
            return MapJson(value)
        return value

    def __repr__(self):
        return str(self.__data)


class Advert(ColourMixin, MapJson):
    repr_color_code = 32  # green
    to_base_colour = 0  # black

    def __init__(self, input_dict):
        super().__init__(input_dict)

        if not self.title:
            raise NameError('The Advert must has a title')

        print(self.__dict__.keys())

        if not self.price:
            self.price = 0
        elif self.price < 0:
            raise ValueError('price must be >= 0')

    def __repr__(self):
        return f'{self.title} | {self.price}'


if __name__ == '__main__':
    # lesson_str = """{
    #                 "title": "python",
    #                 "price": -2,
    #                 "class": "phone",
    #                 "location": {
    #                 "address": "город Москва, Лесная, 7",
    #                 "metro_stations": ["Белорусская", "Маяковская"]
    #                 }
    #                 }"""
    lesson_str = """{
                    "title": "Вельш-корги",
                    "price": 1000,
                    "class": "dogs",
                    "location": {
                    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
                    }
                    }"""
    # lesson_str = '{"title": "python"}'
    lesson = json.loads(lesson_str)
    # lsn1 = MapJson(lesson)
    lsn2 = Advert(lesson)
    print(lsn2.price)
    # print(lsn1)
    print(lsn2.location.address)
    print(lsn2)
