from converter import CurrencyConverter

def get_user_input():
    amount = float(input("Enter amount: "))
    from_currency = input("Enter from: ")
    to_currency = input("Enter to: ")
    return amount, from_currency, to_currency

def main():
    converter = CurrencyConverter()
    try:
        amount, from_currency, to_currency = get_user_input()
        converter, rate = converter.convert(amount, from_currency, to_currency)
        print(f'{amount:2f} {from_currency} = {converter:2f} {to_currency}')
        print(f'Exchange rate: 1 {from_currency} = {rate:4f} {to_currency}')
    except Exception as e:
        print('Error:',e)

if __name__ == '__main__':
    main()
#10