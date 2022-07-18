# encoding: utf-8

# REST API
API_KEY = "PKG3HFCXFA7ETP5R3A6U"
API_SECRET_KEY = "da1js0eoYS6ekGtT4TArEOz8Tn0vRwJFM3PIYOG5"
API_URL = "https://paper-api.alpaca.markets"

stopLossMargin = 0.05 # percentage margin for the stop stop loss
# example 10 - (10*0.05) = 9.5 means that my stoploss is at 9.5$

takeProfitMargin = 0.1 # percentage margin for the take profit
# example: 10 + (10*0.1) = 11 means that my take profit is at 11$

maxSpentEquity = 1000 # total equity to spend in a single operation

# MAX ATTEMPTS SECTION
maxAttemptsCP = 5 # CHECK POSITION
maxAttemptsGCP = 5 # GET CURRENT PRICE

#SLEEP TIMES SECTION
sleepTimeCP = 5 # CHECK POSITION
sleepTimeGCP = 5 # GET CURRENT PRICE
