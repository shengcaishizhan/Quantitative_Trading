# ==============================okex自动交易==============================

import ccxt
# =====创建ccxt交易所
exchange = ccxt.okex()  

# 填写API秘钥
exchange.apiKey = '84190a28-60a9-4dde-b358-159cb0ab622a'
exchange.secret = '82DD72435A4FBC0F951B3D0594685587'
exchange.password = 'quantclass'  # okex在创建第三代api的时候，需要填写一个Passphrase，填写到这里即可
# 若使用其他交易所，请填写其他交易所的apikey
# 务必保管好自己的api，定期更新。

# =====获取账户余额
balance = exchange.fetch_balance()
print(balance)


# =====限价单下单
# 买入
order_info = exchange.create_limit_buy_order('BTC/USDT', 0.0001, 40000)  # 交易对、买卖数量、价格
print(order_info)

# 卖出
# order_info = exchange.create_limit_sell_order('BTC/USDT', 0.0001, 40000)  # 交易对、买卖数量、价格


# =====其他操作
# 下市价单，自动撤单，合约相关操作，等等等等，都可以自动运行


# ==============================币安自动交易==============================

# import ccxt
# import time
# import pandas as pd
# pd.set_option("display.max_rows", 1000)
# pd.set_option('expand_frame_repr', False)

# BINANCE_CONFIG = {
#     'apiKey': 'ckul1ANjHREXg6dqrfiJoCECawOV4IqNeXXdkfuH4Pe4V4Ti6BdJl9SqOHy9z6vp',
#     'secret': 'Cahnq6pmUmMqFi9DD5ixce5eBBUJBeNBR3ls5Nsanl438mK2fowx3F9rZxDJDJ5X',
#     'timeout': 3000,
#     'rateLimit': 10,
#     'hostname': 'fapi.binance.com',  # 无法连接的时候启用
#     'enableRateLimit': False}
# exchange = ccxt.binance(BINANCE_CONFIG)

# # # 单向持仓模式下不需要positionSide
# params = {
#     'side': 'SELL',
#     # 'positionSide': 'LONG',
#     'symbol': 'BTCUSDT',  # 交易币对
#     'type': 'MARKET',
#     # 'price': price,  # 下单价格,在限价单的时候启用，将type换成LIMIT
#     'quantity': 0.001,  # 下单数量
#     'timestamp': int(time.time() * 1000),
#     # lever_rate = '20'  # 以页面设置为准
# }
# order_info = exchange.fapiPrivatePostOrder(params=params)
# print(order_info)


# ==============================火币自动交易==============================

# import pandas as pd
# import ccxt
# pd.set_option("display.max_rows", 1000)
# pd.set_option('expand_frame_repr', False)

# exchange = ccxt.huobipro()

# symbol = 'BTC/USDT' # 此处可修改交易币对，先需将资金转入币币账户
# # 交易所配置
# # 此处填入API相关信息
# HUOBI_CONFIG = {
#             'apiKey': 'd30eb8ee-0f8184f5-5cad21df-rfhfg2mkl3',
#             'secret': 'db447995-4e686102-27fa1f78-788f7',
#         }
# exchange = ccxt.huobipro(HUOBI_CONFIG)

# # 账户信息
# balance = exchange.fetch_balance()
# balance = pd.DataFrame(balance)
# # 下单函数，可修改数量及价格
# order_info = exchange.create_limit_buy_order(symbol=symbol,amount=0.0001, price=40000)
# print(order_info)