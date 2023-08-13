import json
import random
import urllib.request

# Server API URL
QUERY = "http://localhost:8080/query"

# 500 server request
N = 500

def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2  # Calculate the average of bid and ask prices
    return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    if price_b == 0:
        return 0  # Avoid division by zero
    return price_a / price_b

# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in range(N):
        try:
            quotes = json.loads(urllib.request.urlopen(QUERY).read())
        except Exception as e:
            print("Error while fetching data:", e)
            continue

        stock_prices = {}  # Dictionary to store stock prices

        # Calculate and print the data points for each stock
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            stock_prices[stock] = price
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

        # Calculate and print the ratio of the two stock prices
        stock_a = 'ABC'
        stock_b = 'DEF'
        if stock_a in stock_prices and stock_b in stock_prices:
            ratio = getRatio(stock_prices[stock_a], stock_prices[stock_b])
            print("Ratio %s" % ratio)
        else:
            print("One or both stocks not found.")

        print("-----------------------")
