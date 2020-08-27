from django.test import TestCase, Client


# Create your tests here.

class CurrencyExchangeTestCase(TestCase):
    fixtures = ['test_rates.json']

    def setUp(self):
        super().setUp()
        self.client = Client()

    def test_exchange_form(self):
        response = self.client.get('/exchange/')

        self.assertContains(response, '<input name="value" type="number" required maxlength="100" />')
        self.assertContains(response, '<select name="currency_from" required><option value="1">USD</option><option value="2">BYN</option></select>')
        self.assertContains(response, '<select name="currency_to" required><option value="1">USD</option><option value="2">BYN</option></select>')

    def test_exchange_calculate(self):
        response = self.client.post("/exchange/", data={
            'currency_from': '1',
            'currency_to': '2',
            'value': '100',
        })

        self.assertContains(response, '<span class="result">260</span>')