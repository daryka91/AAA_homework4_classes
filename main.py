import json
import keyword


class ColorMixin:

    def __str__(self):
        return f"\033[1;33;20m {self.title} | {self.price}\033[0;0;0m"


class MapJson:
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


class Advert(ColorMixin, MapJson):

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
    # lesson_str = """{
    #                 "title": "Вельш-корги",
    #                 "price": 1000,
    #                 "class": "dogs",
    #                 "location": {
    #                 "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
    #                 }
    #                 }"""
    lesson_str = '{"title": "python"}'
    lesson = json.loads(lesson_str)
    lsn = MapJson(lesson)
    lsn1 = Advert('title', -5)  # конфликта нет, потому что
    print(lsn1)
    print(lsn.class_)


