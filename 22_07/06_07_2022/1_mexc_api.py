# 1. pip install ccxt

import ccxt
import pprint

exchange = ccxt.mexc()
pando_usdt = exchange.fetch_ticker("PANDO/USDT")
pando_usd = float(pando_usdt['ask'])
print(pando_usd)

eth_usdt = exchange.fetch_ticker("ETH/USDT")
eth_usd = float(eth_usdt['ask'])
print(eth_usd)

btc_usdt = exchange.fetch_ticker("BTC/USDT")
btc_usd = float(btc_usdt['ask'])
print(btc_usd)

# m판도 -> 이더
b = 20 * pando_usd

# 1 : eth_usd == x : b

# ex)
print(b)

x = b / eth_usd

print(x)

result = 0.00001816 * 20 

print(result)
# 1 : 1,137.88$ == x : 25$

# x = 25$ // 1,137.88$ (약 0.022개)

# -----------------------------------------------------------------------------------------------------------

# # m판도 -> 비트

# 1 : a('비트코인 가격') == x : b('유저가 가지고 있는 m판도 가격')

# # ex)

# 1 : 20,197.47$ = x : 27$

# x = 27$ // 20,197.47$ (약 0.0013368개)
# # -----------------------------------------------------------------------------------------------------------

# # 이더 -> m판도
# b('유저가 가지고있는 이더 수의 대한 가격') = ('유저의 이더 개수') * ('실시간 이더 가격')

# 1('m판도 한개') : 27('실시간 m판도 가격') == x : b('유저가 가지고있는 이더 수의 대한 가격')

# # ex)

# 1 : 27 = x : 1,137.88$

# x = 1,137.88 // 27 (약 3.7개)
# # -----------------------------------------------------------------------------------------------------------

# # 비트 -> m판도
# b('유저가 가지고있는 비트 수의 대한 가격') = ('유저의 비트 개수') * ('실시간 비트 가격')

# 1('m판도 한개') : 27('실시간 m판도 가격') == x : b('유저가 가지고 있는 비트 수의 대한 가격')

# # ex)

# 1 : 27 = x : 26,388,503$

# x = 11,082.96$ // 27 (약 410개)