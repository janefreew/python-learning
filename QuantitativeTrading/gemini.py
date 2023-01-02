
########## GEMINI行情接口 ##########
## https://api.gemini.com/v1/pubticker/:symbol

import json
import requests

gemini_ticker = 'https://api.gemini.com/v1/pubticker/{}'

bigquant_ticker = 'https://bigquant.com/wiki/doc/jiekou-qsctulIh0x/{}'
symbol = 'btcusd'
# btc_data = requests.get(gemini_ticker.format(symbol)).json()
btc_data = requests.get(bigquant_ticker.format(symbol)).json()
print(json.dumps(btc_data, indent=4))

########## 输出 ##########
