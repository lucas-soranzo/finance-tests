import yfinance as yf

msft = yf.Ticker("BOVA11.SA")

# get stock info
print(msft.info)

# get historical market data
hist = msft.history(period="max")
print(hist)