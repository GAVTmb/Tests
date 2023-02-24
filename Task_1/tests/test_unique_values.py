from unittest import TestCase
from Task_1.unique_values import unique_values

param_test = {
    '1': [33, 16, 168, 3],
    '2': [33, 236],
    '6': [168, 33, 3, 16, 3]
}

rsault = [33, 16, 168, 3, 236]


class TestTask1(TestCase):
    def test_unique_values(self):
        param = param_test
        res = unique_values(param)
        self.assertEqual(res, rsault)
