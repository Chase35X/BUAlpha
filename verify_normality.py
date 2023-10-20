import yfinance as yf
import scipy.stats as stats

# input ticker here
ticker = 'MSFT'

# stock object for ticker
stock = yf.Ticker(ticker)

# dates
start_date = "2020-06-02"
end_date = "2020-07-29"

# history of stock prices from dates inputted -> turn open prices into list
stock_history = stock.history(start=start_date, end=end_date)
prices = stock_history["Open"]
prices = prices.tolist()

# calculate p value using Shapiro test
p = stats.shapiro(prices).pvalue
alpha = 0.05

# if p is high null will fly, if p is low the null must go
if p>alpha:
    print("Distribution is normal considering p > alpha")
else:
    print("Distribution is not normal considering p < alpha")

# additional information
print(f"p = {p}")
print(f"alpha level = {alpha}")

# table print
stock_price_array = stock_history["Open"].array

print()
print("Stock Price Summary (Weekly High)")
for price in stock_price_array[::7]:
    print(f"{price:.3f}", end="\t")
