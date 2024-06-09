from datetime import datetime

from lumibot.backtesting import YahooDataBacktesting
from lumibot.brokers import Alpaca
from lumibot.strategies.strategy import Strategy
from lumibot.traders import Trader


# API_KEY ='PKQ8MBFEEZV1JR7XDCFT'
# API_SECRETE = 'OSKBfTVa8maYXVLtGCCEkY7368bRNXwwaJX6mnqC'
# BASE_URL = 'https://paper-api.alpaca.markets/v2'

# ALPACA_CRED ={
#     'API_KEY':API_KEY,
#     'API_SECRETE':API_SECRETE,
#     'PEPER':True
# }
ALPACA_CONFIG = {
    "API_KEY": "PK4CRFVMD6T9A8WPS6CT",
    "API_SECRET": "WziihsdnUBBqLui5u6nC3gjbySohVt7HR44fUmY4",
    "ENDPOINT": "https://paper-api.alpaca.markets/v2"
}

class MyStrategy(Strategy):
    # Custom parameters
    parameters = {
        "symbol": "SPY",
        "quantity": 1,
        "side": "buy"
    }

    def initialize(self, symbol=""):
        # Will make on_trading_iteration() run every 180 minutes
        self.sleeptime = "180M"

    def on_trading_iteration(self):
        symbol = self.parameters["symbol"]
        quantity = self.parameters["quantity"]
        side = self.parameters["side"]

        order = self.create_order(symbol, quantity, side)
        self.submit_order(order)


trader = Trader()
broker = Alpaca(ALPACA_CONFIG)
strategy = MyStrategy(
    broker=broker,
    parameters= {
        "symbol": "SPY"
    })

# Backtest this strategy
backtesting_start = datetime(2020, 1, 1)
backtesting_end = datetime(2020, 12, 31)
strategy.backtest(
    YahooDataBacktesting,
    backtesting_start,
    backtesting_end,
    # You can also pass in parameters to the backtesting class, this will override the parameters in the strategy
    parameters= {
        "symbol": "SPY"
    },
)

# Run the strategy live
trader.add_strategy(strategy)
trader.run_all()