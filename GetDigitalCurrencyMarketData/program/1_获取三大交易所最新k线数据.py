import pandas as pd
from datetime import timedelta
import ccxt
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 5000)  # 最多显示数据的行数
# 刚开始学习编程时，讲究'好读书不求甚解'，少问为什么，能解决问题就行


# =====创建ccxt交易所
# exchange = ccxt.okex()   # okex
# exchange = ccxt.huobipro()  # 火币
exchange = ccxt.binance()  # 币安


# =====设定参数
symbol = 'BTC/USDT'   # 抓取的品种。btc/usdt现货交易对。其他币种照例修改即可，例如ETH/USDT，LTC/USDT等
time_interval = '15m'  # K线的时间周期，其他可以尝试的值：'1m', '5m', '15m', '30m', '1h', '2h', '1d', '1w', '1M', '1y'，并不是每个交易所都支持


# =====获取最新数据
data = exchange.fetch_ohlcv(symbol=symbol, timeframe=time_interval)  # fetch_ohlcv一句话搞定。过程中要联网。


# =====整理数据
df = pd.DataFrame(data, dtype=float)  # 将数据转换为dataframe
df.rename(columns={0: 'MTS', 1: 'open', 2: 'high',
                   3: 'low', 4: 'close', 5: 'volume'}, inplace=True)  # 重命名
df['candle_begin_time'] = pd.to_datetime(df['MTS'], unit='ms')  # 整理时间
df['candle_begin_time_GMT8'] = df['candle_begin_time'] + timedelta(hours=8)  # 北京时间
df = df[['candle_begin_time_GMT8', 'open', 'high', 'low', 'close', 'volume']]  # 整理列的顺序

print(df)  # 打印数据


# =====保存数据到本地
df.to_csv('xingbuxing_data.csv', index=False)
