from django.test import TestCase

from orderapp.models import OrderRecord
# Create your tests here.

import random


class TestOrderRecord(TestCase):

    def test_insert(self):
        for month in range(4, 10):
            for day in range(10, 21):
                orObj = OrderRecord()
                orObj.date = f'2018-0{month}-{day}'
                orObj.order_count = random.randint(1000,
                                                   2000)
                orObj.order_cancel_count = random.randint(10, 200)
                orObj.order_price = random.uniform(1000000, 5000000)
                orObj.order_cancel_price = random.uniform(10000, 200000)
                orObj.save()
                print('------')
