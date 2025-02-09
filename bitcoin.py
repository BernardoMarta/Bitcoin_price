import requests
import sys

if len(sys.argv) < 2:
        sys.exit('Command-line argument is missing')
try:
        USD = float(sys.argv[1])
        bitcoin_price = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
        usdbitcoin_rate = bitcoin_price['bpi']['USD']['rate_float']
        bitcoin_calculated = USD*usdbitcoin_rate
        print(f'${bitcoin_calculated:,.4f}')

except ValueError:
    sys.exit('Command-line argument is not a number')
