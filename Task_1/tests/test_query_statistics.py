from unittest import TestCase
from Task_1.query_statistics import query_statistics

param_test = [
    'Как управлять миром',
    'Как стать самым умным',
    'Что посмотреть вечером',
    'Топ сериалов',
    'Онлайн курсы',
    'Что происходит зарубежом'
]

rsault = [
    'Запросов из 3 слов - 50%',
    'Запросов из 4 слов - 17%',
    'Запросов из 2 слов - 33%'
]


class TestTask1(TestCase):
    def test_query_statistics(self):
        param = param_test
        res = query_statistics(param)
        self.assertEqual(res, rsault)
