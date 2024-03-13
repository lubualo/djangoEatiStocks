from .models import Investment, Stock
import yfinance as yf

def getInvestmentsWithCurrentPrice():
  CURRENT_STOCK_PRICES = {}
  for stock in Stock.objects.all():
    stockData = yf.Ticker(stock.ticker)
    historical_prices = stockData.history(period='1d', interval='1m')
    # Get the latest price and time
    latest_price = historical_prices['Close'].iloc[-1]
    CURRENT_STOCK_PRICES[stock.ticker] = latest_price
  investments = []
  for investment in Investment.objects.all():
    investments.append({
      "id": investment.id,
      "ticker": investment.stock.ticker,
      "date": investment.date,
      "quantity": investment.quantity,
      "pricePerUnit": investment.pricePerUnit,
      "currentPrice": CURRENT_STOCK_PRICES[investment.stock.ticker]
    })
  return investments
