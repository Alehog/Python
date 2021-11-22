import yfinance as yf
from datetime import date
import pandas as pd
class portfolioData:
    def __init__(self, stocks_input = [], weights = [], start_date = "2019-01-01", end_date = date.today().strftime("%Y-%m-%d"), 
                 description = ""):
        self.description = description
        self.stocks = {}
        self.weights = {}
        for i, stock in enumerate(stocks_input):
            weight = weights[i]/sum(weights)
            self.stocks[stock] = self.stockData(stock, start_date, end_date)
            self.weights[stock] = weight
    def updateAll(self):
        for stock in self.stocks.keys():
            self.stocks[stock].current_price = self.stocks[stock].getCurrentPrice()
            
    def listAllPrices(self):
        for stock in self.stocks.keys():
            print(stock, ": ", self.stocks[stock].current_price, sep = "")
    
    def listAllWeights(self):
        for stock in self.weights.keys():
            print(stock, ": ", self.weights[stock], sep = "")
            
    def addStock(self, stock, weight, start_date = "2019-01-01", end_date = date.today().strftime("%Y-%m-%d")):
        self.updateWeights(weight = weight)
        self.stocks[stock] = self.stockData(ticker = stock, start_date = start_date, end_date = end_date)
        self.weights[stock] = weight
    
    def updateWeights(self, weight):
        for stock in self.weights.keys():
            new_weight = self.weights[stock]*(1-weight)
            self.weights[stock] = new_weight
    
    def historicPortfolio(self):
        stock_prices = None
        for stock in self.stocks.keys():
            if stock_prices is None:
                stock_prices = self.stocks[stock].historic_data["Close"]
                stock_prices = stock_prices.rename(stock)
                weights = stock_prices.copy()
                weights.loc[stock] = self.weights[stock]
            else:
                temp = self.stocks[stock].historic_data["Close"]
                stock_prices = pd.merge(stock_prices, temp, how = "outer", 
                              left_index = True, right_index = True)
                stock_prices = stock_prices.rename(columns = {"Close":stock})
                temp.loc["Close"] = self.weights[stock]
                weights = pd.merge(weights, temp, how = "outer", 
                              left_index = True, right_index = True)
        
        return weights


    class stockData:
        def __init__(self, ticker, start_date, end_date):
            self.ticker = ticker
            data = self.connection()
            self.current_price = self.getCurrentPrice(data)
            self.historic_data = self.getHistoricPrice(start_date, end_date, data)
            self.start_date = start_date
            self.end_date = end_date
            
        def connection(self):
            return yf.Ticker(self.ticker)
            
        def getCurrentPrice(self, data = None):
            if data == None:
                data = self.connection()
            return data.info["currentPrice"]
        
        def getHistoricPrice(self, start_date = None, end_date = None, data = None):
            if data == None:
                data = self.connection()
            if start_date == None:
                start_date = self.start_date
            if end_date == None:
                end_date = self.end_date
            return data.history(start = start_date, end = end_date)
            
portfolio1 = portfolioData(["MSFT"], weights = [1], start_date="2020-01-01")
portfolio1.addStock("AAPL", 0.5)
