from .models import Investment, Stock
import yfinance as yf


def getInvestmentsWithCurrentPrice():
    CURRENT_STOCK_PRICES = {}
    for stock in Stock.objects.all():
        stockData = yf.Ticker(stock.ticker)
        historical_prices = stockData.history(period="1d", interval="1m")
        # Get the latest price and time
        latest_price = historical_prices["Close"].iloc[-1]
        CURRENT_STOCK_PRICES[stock.ticker] = latest_price
    investments = []
    for investment in Investment.objects.all():
        investments.append(
            {
                "id": investment.id,
                "ticker": investment.stock.ticker,
                "date": investment.date,
                "quantity": f"{investment.quantity:.2f}",
                "pricePerUnit": f"{investment.pricePerUnit:.2f}",
                "currentPrice": f"{CURRENT_STOCK_PRICES[investment.stock.ticker]:.2f}",
                "interest": f"{(CURRENT_STOCK_PRICES[investment.stock.ticker] / investment.pricePerUnit - 1):.2%}",
            }
        )
    return investments


def getTickerInfo(ticker: str):
    ticker = yf.Ticker(ticker.upper())
    tickerHistory = ticker.history()
    if "Empty DataFrame" in str(tickerHistory):
        return None
    else:
        return ticker.info


def isNewTicker(ticker: str):
    try:
        Stock.objects.get(ticker=ticker)
        return False
    except Stock.DoesNotExist:
        return True


def getTickersList():
    tickersInfo = []
    for stock in Stock.objects.all():
        tickerInfo = getTickerInfo(stock.ticker)
        tickersInfo.append(tickerInfo)
    return tickersInfo
