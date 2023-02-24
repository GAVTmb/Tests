from unittest import TestCase
from Task_2.upload_yandex import upload



param_test = 'TEST'

rsault = [f'https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2F'
          f'{param_test}', 201]


class TestYaUpload(TestCase):
    def test_upload(self):
        param = param_test
        res = upload(param)
        self.assertEqual(res, rsault)
