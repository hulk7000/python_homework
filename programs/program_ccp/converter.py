from currency_dict import EXCHANGE_RATES

class CurrencyConverter:
    def __init__(self):
        self.rates = EXCHANGE_RATES

    def convert(self, amount, from_currency, to_currency):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in self.rates or to_currency not in self.rates[from_currency]:
            raise ValueError(f'No conversion rate from {from_currency} to {to_currency}')

        rate = self.rates[from_currency][to_currency]
        converted_amount = amount * rate
        return converted_amount,rate