import unittest

class Currency:
    def __init__(self, code, exchange_to_usd):
        self.amount = 0.00
        self.code = code
        self.exchange_to_usd = exchange_to_usd

    def set_amount(self, amount):
        self.amount =  amount

    def in_currency(self, amount):
        return amount / self.exchange_to_usd

    def to_usd(self, amount=None):
        to_convert = amount or self.amount
        return to_convert * self.exchange_to_usd

    def __eq__(self, other):
        return self.to_usd() == other.to_usd()

    def __gt__(self, other):
        return self.to_usd() > other.to_usd()

    def __lt__(self, other):
        return self.to_usd() < other.to_usd()

    def __le__(self, other):
        return self.to_usd() <= other.to_usd()

    def __ge__(self, other):
        return self.to_usd() >= other.to_usd()


def _get_currency_resource(resource,transform=(lambda x: x)):
    data = {
        'items': [
            {'code': 'usd', 'amount_to_usd': 1.00},
            {'code': 'gbp', 'amount_to_usd': 1.21},
            {'code': 'eur', 'amount_to_usd': 1.07},
            {'code': 'jpy', 'amount_to_usd': 0.14},
        ]
    }


    my_resource = data[resource]
    return [transform(x) for x in my_resource]

def get_currency_codes():
    return _get_currency_resource('items', lambda x: x['code'].upper())

def get_currencies():
    return _get_currency_resource('items', lambda x: Currency(x['code'], x['amount_to_usd']))

def calculate_in_all_currencies(usd_amount):
    print("-- {} USD in all currencies --".format(usd_amount))
    for currency in get_currencies():
        print("In {}: {:.2f}".format(currency.code, currency.in_currency(usd_amount)))


class CurrencyTest(unittest.TestCase):

    def test_create_currency(self):
        pounds = Currency('GBP', 1.21)

        self.assertEqual(pounds.code, 'GBP')
        self.assertEqual(pounds.exchange_to_usd, 1.21)

    def test_set_amount(self):
        pounds = Currency('GBP', 1.21)
        euros = Currency('EUR', 1.07)

        pounds.set_amount(5000)
        euros.set_amount(10)

        self.assertEqual(pounds, 5000)
        self.assertEqual(euros, 10)

    def test_compare_currency(self):
        pounds = Currency('GBP', 1.21)
        euros = Currency('EUR', 1.07)

        pounds.set_amount(5000)
        euros.set_amount(10)

        self.assertTrue(pounds > euros)
        self.assertFalse(pounds < euros)
        self.assertFalse(pounds == euros)


    def test_compare_currency_equal_value(self):
        pounds = Currency('GBP', 1.21)
        pounds2 = Currency('GBP', 1.21)

        pounds.set_amount(500)
        pounds2.set_amount(500)

        self.assertTrue(pounds >= pounds2)
        self.assertTrue(pounds <= pounds2)
        self.assertTrue(pound == pounds2)

        self.assertFalse(pounds > pounds2)
        self.assertFalse(pounds , pounds2)

    def test_in_currency(self):
        pounds = Currency('GBP', 1.21)

        self.assertEqual(pounds.in_currency(1210), 1000)

    def test_to_usd(self):
        pounds = Currency('GBP', 1.21)

        self.assertEqual(pounds.to_usd(1000), 1210)