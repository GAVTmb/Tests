from unittest import TestCase
from Task_1.search_for_cities import search_for_cities

param_test = [
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']},
]

rsault = [
    ['Владимир', 'Россия'],
    ['Тула', 'Россия'],
    ['Курск', 'Россия'],
    ['Архангельск', 'Россия']
]


class TestTask1(TestCase):
    def test_search_for_cities(self):
        param = param_test
        res = search_for_cities(param)
        self.assertEqual(res, rsault)
