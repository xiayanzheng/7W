from forex_python.converter import CurrencyRates

def exchange_rate():
        c = CurrencyRates()
        print(c.convert('CNY', 'JPY', 1))

exchange_rate()