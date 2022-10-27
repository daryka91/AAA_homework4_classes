import json
import keyword


class ColorMixin:
    """окрашивает текст"""
    repr_colour = '\033[33m'  # желтый
    to_base_colour = '\033[0m'  # конец окрашивания

    def __str__(self):

        return f'{self.repr_colour}{self.title} | {self.price}{self.to_base_colour}'


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


class Advert( MapJson):

    def __init__(self, title, price1=0, input_dict={}):
        super().__init__(input_dict)
        self.title = title
        self.price = price1

    @property
    def price(self):
        return self.price_value if self.price_value else 0

    @price.setter
    def price(self, price2):
        if price2 < 0:
            raise ValueError("must be >= 0")
        else:
            self.price_value = price2

    def __repr__(self):
        # colour_beauty, colour_base = super().__repr__().split()
        # return colour_beauty + f'{self.title} | {self.price} ' + colour_base
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
    lsn1 = Advert('title', 1000, lesson)  # конфликта нет, потому что
    print(lsn1)
    print(lsn1.class_)


