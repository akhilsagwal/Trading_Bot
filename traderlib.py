# encoding: utf-8

#import alpaca_trade_api as tradepi

import sys , os, time, pytz
import tulipy as ti
import pandas as pd
from datetime import datetime
from math import ceil




class Trader:

    def __init__(self, ticker):
        lg.info('Trader initialized with ticker %s' % ticker)
        self.ticker = ticker   # assign external variable to internal


    def is_tradeable(self,ticker):

        # ask the broker/API if "ticker" is tradeable
            # IN: ticker (string)
            # OUT: True(tradeable) / False(not tradeable)

        try:
            # ticker =  get ticker from alpaca wrapper (.tradeable)
            if not ticker.tradeable:
                lg.info(' The ticker %s is not tradeable' % ticker)
                return False
            else:
                lg.info('The ticker %s is tradeable!' % ticker)
                return True

        except:
            lg.error('The ticker %s is not answering well' % ticker)
            return False

    def set_stoploss(self,entryPrice,trend):

    # takes an entry price as a input and sets the stoploss (trend)
                # IN: entry price, trend (long/short)
                # OUT:stoploss

        try:
            if trend == 'long':
                # example 10 - (10*0.05) = 9.5
                stopLoss = entryPrice - (entryPrice * gvars.stopLossMargin)
                return stopLoss

            elif trend == 'short':
                # example 10 + (10*0.05) = 10.5

                stopLoss = entryPrice + (entryPrice * gvars.stopLossMargin)
                return stopLoss

            else:
                raise ValueError

        except Exception as e:
            lg.error('The trend value is not understood: %s' % str(trend))
            sys.exit()

    def set_takeprofit(self,entryPrice,trend):

        # set take profit: takes a price as an input and sets the takeprofit
            # IN: entry price,trend (long/short)
            # OUT: take takeprofit


        try:
            if trend == 'long':
                # example 10 + (10*0.1) = 11
                takeProfit = entryPrice + (entryPrice * gvars.takeProfitMargin)
                lg.info('Take profit set for long at %.2f' % takeProfit)
                return takeProfit

            elif trend == 'short':
                # example 10 - (10*0.1) = 9
                takeProfit = entryPrice - (entryPrice * gvars.takeProfitMargin)
                lg.info('Take profit set for short at %.2f' % takeProfit)
                return takeProfit

            else:
                raise ValueError

        except Exception as e:
            lg.error('The trend value is not understood: %s' % str(trend))
            sys.exit()

    # load historical stock data:
        # IN: ticker, interval, entries limit
        # OUTL array with stock data(OHCL)

    def get_open_poisitions(self,tickerId):
        # get open posiitons
            # IN: tickerId (unique identifier)
            # OUT: boolean( True = already open, False = not open)

        # posiitons = ask alpaca wrapper for the list of open positions
        for position in positions:
            if position.symbol == tickerId:
                return True

            else:
                return False

    # submit order: gets our order through the API (loop/retry)
        # IN: order data (number of shares), order type
        # OUT: boolean (True = order went through, False = order did not)

    # cancel order: cancels our order (retry)
        # IN: order id
        # OUT: boolean (True = order cancelled, False = order not cancelled)

    def check_position(self,ticker,doNotFind=False):

        # check position: check whether the position exists or not
          # IN: ticker, doNotFind (means that I dont want to find)
          # OUT: boolean (True = order is there, False = order not there)

          attempt = 1

          while attempt < gvars.maxAttemptsCP:
            try:
                    # position = ask the alpaca wrapper for a position
                currentPrice = position.current_price
                lg.info('The position was checked. Current price is: %.2f' % currentPrice)
                return True
            except:

                if doNotFind:
                    lg.info('Position not found, this is good!')
                    return False

                lg.info('Position not found, waiting for it...')
                time.sleep(gvars.sleepTimeCP) # wait 5 seconds and retry
                attempt += 1

            lg.info('Position not found for %s, not waiting any more' % ticker)
            return False

    def get_shares_amount(self,tickerPrice):
        # works out the number of shared I want to buy/sell
            # IN: tickerPrice
            # OUT: number of shares

        lg.info('Getting shares amount')

        try:
            # define max to spend

            # get the total equity available
            # totalEquity = ask Alpaca API for available equity

            # calculate the number of shares
            sharesQuantity = int(gvars.maxSpentEquity / tickerPrice)

            lg.info('Total shares to operate with: %d' % sharesQuantity)

            return sharesQuantity

        except Exception as e:
            lg.error('Something happened at get shares amount')
            lg.error(e)
            sys.exit()

    def get_current_price(self,ticker):
        #get the current price of an ticker with a position open
            # IN: ticker
            # OUT: price($)


        attempt = 1

        while attempt < gvars.maxAttemptsGCP:
            try:
                # position = ask the alpaca wrapper for a position
                currentPrice = position.current_price
                lg.info('The position was checked. Current price is: %.2f' % currentPrice)
                return currentPrice
            except:
                lg.info('Position not found, cannot check price, waiting for it...')
                time.sleep(gvars.sleepTimeGCP) # wait 5 seconds and retry
                attempt += 1

        lg.info('Position not found for %s, not waiting any more' % ticker)
        return False

    def get_general_trend(self,ticker):

    # get general trend: detect interseting trend (UP / DOWN / False if no trend)
        # IN: ticker
        # OUTPUT: UP / DOWN / NO TREND (strings)
        #If no trend defined, go back to POINT ECHO

        lg.info('GENEEAL TREND ANALYSIS entered')

        attempt = 1
        maxAttempts = 10 # total time = maxAttempts * 60s (as implemented)

        try:

            while True:

                # data = ask Alpaca wrapper for 30 min candles


                # calculate the EMAs
                ema9 = ti.ema(data, 9)
                ema26 =  ti.ema(data, 26)
                ema50 = ti.ema(data, 50)

                # checking EMAs relative position
                # if (ema50 > ema26) and (ema26 > ema9):
                lg.info('Trend detected for %s: long' % ticker)
                return 'long'
                # elif (ema50 < ema26) and (ema50 < ema9):
                lg.info('Trend detected for %s: short' % ticker)
                return 'short'
                # elif attempts <= maxAttempts:
                lg.info('Trend not clear for %s, waiting...' % ticker)
                attemp += 1
                time.sleep(60)
                # else:
                lg.info('Trend NOT detected for %s' % ticker)
                return False

        except Exception as e:
            lg.error('Something went wrong at get general trend')
            lg.error(e)
            sys.exit()

    def get_insant_trend(self,ticker,trend):

        # get instant trend: confirm the trend detected by GT analysis
            # IN: ticker, trend (long / short)
            # OUT: True(trend confirmed) / False(not a good moment to enter)

        lg.info('INSTANT TREND ANALYSIS entered')

        attempt = 1
        maxAttempts = 10 # total time = maxAttempts * 30s (as implemented)

        try:
            while True:
                # data = ask Alpaca wrapper for 5 min candles

                # calculate the EMAs
                ema9 = ti.ema(data, 9)
                ema26 =  ti.ema(data, 26)
                ema50 = ti.ema(data, 50)

                lg.info('%s instant trend EMAs: [%.2f,%.2f,%.2f]' % (ticker,ema9, ema26, ema50))


                if (trend== 'long') and (ema9 > ema26) and (ema26 > ema50):
                    lg.info('Long trend confirmed for %s' % ticker)
                    return True
                elif (trend == 'short') and (ema9 < ema26) and (ema26 < ema50):
                    lg.info('Short trend confirmed for %s' % ticker)
                    return True
                elif attempt <= maxAttempts:
                    lg.info('Trend not clear for %s, waiting...' % ticker)
                    attemp += 1
                    time.sleep(30)
                else:
                    lg.info('Trend NOT detected for %s' % ticker)
                    return False

        except Exception as e:
            lg.error('Something went wrong at get instant trend')
            lg.error(e)
            sys.exit()

    def get_rsi(self,ticker,trend):

        # get rsi: perform RSI analysis
            # IN: 5 min candles data (Closed data), output of the GT analysis(UP / DOWN string)
            # OUT: True(confirmed) / False(not confirmed)

            lg.info('RSI ANALYSIS enterd')

            attempt = 1
            maxAttempts = 10 # total time = maxAttempts * 20s (as implemented)

            try:
                while True:
                    # data = ask Alpaca wrapper for 5 min candles

                    # calculate the RSIs
                    rsi = ti.rsi(data, 14) # it uses 14-sample window


                    lg.info('%s rsi = [%.2f]' % (ticker,rsi))


                    if (trend== 'long') and (rsi > 50) and (rsi < 80):
                        lg.info('Long trend confirmed for %s' % ticker)
                        return True
                    elif (trend == 'short') and (rsi < 50) and (rsi > 20):
                        lg.info('Short trend confirmed for %s' % ticker)
                        return True
                    elif attempt <= maxAttempts:
                        lg.info('Trend not clear for %s, waiting...' % ticker)
                        attemp += 1
                        time.sleep(20)
                    else:
                        lg.info('Trend NOT detected for %s' % ticker)
                        return False

            except Exception as e:
                lg.error('Something went wrong at rsi analysis')
                lg.error(e)
                sys.exit()

    def get_stochastic(self,ticker,trend):

        # get stochastic: perform STOCHASTIC analysis
            # IN: ticker, trend
            # OUT: True(confirmed) / False(not confirmed)

        lg.info('STOCHASTIC ANALYSIS entered')

        attempt = 1
        maxAttempts = 20 # total time = maxAttempts * 10s (as implemented)

        try:
            while True:
                # data = ask Alpaca wrapper for 5 min candles

                # calculate the STOCHASTIC
                stoch_k, stoch_d = ti.stoch(high, low, close, 9, 6, 9)

                lg.info('%s stochastic = [%.2f,%.2f]' % (ticker,stoch_k,stoch_d))


                if (trend== 'long') and (stoch_k > stoch_d) and (stoch_k < 80) and (stoch_d < 80):
                    lg.info('Long trend confirmed for %s' % ticker)
                    return True
                elif (trend == 'short') and (stoch_k < stoch_d) and (stoch_k > 20) and (stoch_d < 20):
                    lg.info('Short trend confirmed for %s' % ticker)
                    return True
                elif attempt <= maxAttempts:
                    lg.info('Trend not clear for %s, waiting...' % ticker)
                    attemp += 1
                    time.sleep(10)
                else:
                    lg.info('Trend NOT detected for %s' % ticker)
                    return False

        except Exception as e:
            lg.error('Something went wrong at stochastic analysis')
            lg.error(e)
            sys.exit()

    def check_stochastic_crossing(self,ticker,trend):
        # check whether the stochastic curves have crossed or not
        # depending on the trend
            # IN: ticker, trend
            # OUT: True if crossed / False if not crossed

        lg.info('Checking stochastic crossing...')

        # getting stochastic values
        # data = ask Alpaca wrapper for 5 min candles

        # calculate the STOCHASTIC
        stoch_k, stoch_d = ti.stoch(high, low, close, 9, 6, 9)

        lg.info('%s stochastic = [%.2f,%.2f]' % (ticker,stoch_k,stoch_d))

        try:
            if (trend=='long') and (stoch_k <= stoch_d):
                lg.info('Stochastic curves crossed: long, k=%.2f, d=%.2f' % (stoch_k,stoch_d))
                return True
            elif (trend=='short') and (stoch_k >= stoch_d):
                lg.info('Stochastic curves crossed: short, k=%.2f, d=%.2f' % (stoch_k,stoch_d))
                return True
            else:
                lg.info('Stochastic curves have not crossed')
                return False

        except Exception as e:
            lg.error('Something went wrong at check stochastic crossing')
            lg.error(e)
            return True

    def enter_position_mode(self,ticker,trend):
        # check the conditions in parallel once inside the position

            attempts = 1
            maxAttempts = 1260 # calculate 7h total: 7*60*60 / 20

            # entryPrice = ask the Alpaca API for the entry price

            # set the takeprofit
            takeProfit = set_takeprofit(entryPrice,trend)

            # set the stoploss
            stopLoss= set_stoploss(entryPrice,trend)

            try:
                while True:

                    currentPrice = get_current_price(ticker)

                    #check if take profit met
                    # LONG/UP version
                    if (trend=='long') and currentPrice >= takeProfit:
                        lg.info('Take profit met at %.2f. Current price is %.2f' % (takeProfit,currentPrice))
                        return True

                    # SHORT/DOWN version
                    elif (trend=='short') and currentPrice <= takeProfit:
                        lg.info('Take profit met at %.2f. Current price is %.2f' % (takeProfit,currentPrice))
                        return True

                    # check if stop loss is met
                    #LONG/UP version
                    elif (trend=='long') and currentPrice <= stopLoss:
                        lg.info('Stop loss met at %.2f. Current price is %.2f' % (stopLoss,currentPrice))
                        return False

                    #SHORT/DOWN version
                    elif (trend=='short') and currentPrice >= stopLoss:
                        lg.info('Stop loss met at %.2f. Current price is %.2f' % (stopLoss,currentPrice))
                        return False

                    # check stoch crossing
                    elif check_stochastic_crossing(ticker,trend):
                        lg.info('stochastic curves crossed. Current price is %.2f' % currentPrice)
                        return True

                    elif attempt <= maxAttempts:
                        lg.info('Waiting inside position, attempt %d' % attempt)
                        lg.info('%.2f <-- %.2f --> %.2f' % (stopLoss,currentPrice,takeProfit))
                        time.sleep(20)
                        attempts += 1



                    # get out, time is out
                    else:
                        lg.info('Timeout reached at enter position too late')
                        return False

            except Exception as e:
                lg.error('Something happened at enter position function')
                lg.error(e)
                return True




    def run(self):

        #LOOP until timeout reached (ex. 2h)
        while True:

             #POINT ECHO: INITIAL CHECK
            # ask the broker/API if we have an open position with ticker
            if check_position(self.ticker,doNotFind=True):
                lg.info('There is already an open position with that ticker! Aborting...')
                return False # aborting execution


            # POINT DELTA

            while True:

                # find general trend
                trend = get_general_trend(self.ticker)
                if not trend:
                    lg.info('No general trend found for %s! Going out...' % self.ticker)
                    return False # aborting execution

                # confirm instant trend
                if not get_insant_trend(self.ticker,trend):
                    lg.info('The instant trend is not confirmed. Going back.')
                    continue # if failed go back to POINT DELTA

                # perform RSI  analysis
                if not get_rsi(self.ticker,trend):
                    lg.info('The rsi is not confirmed. Going back.')
                    continue # if failed go back to POINT DELTA

                # perform STOCHASTIC analysis
                if not get_stochastic(self.ticker,trend):
                    lg.info('The rsi is not confirmed. Going back.')
                    continue # if failed go back to POINT DELTA

                lg.info('All filtering passed, carrying on with the order!')
                break # get out of the loop

            # get_current_price
            self.currentPrice=get_current_price(self.ticker)

            # get_shares_amount: decide the total amount to invest
            sharesQuantity = get_shares_amount(self.ticker,self.currentPrice)

            # submit order(limit)
                # if false, abort / go back to point ECHO

            # check position
            if not check_position(self.ticker):
                # cancel pedning order
                continue # go back to POINT ECHO

            # enter position mode
            successfulOperation = enter_position_mode(ticker,trend)


            #GET OUT
            while True:
                # submit order(market)

                # check the position is cleared
                if not check_position(self.ticker,doNotFind=True):
                    break

                time.sleep(10) # wait 10 seconds
                # check position is not there (with doNotFind=TRUE)
                    # wait for a False, then get out


            # end of execution
            return successfulOperation
