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

    def is_tradeable(self,ticker):

        # ask the broker/API if "asset" is tradeable
            # IN: asset (string)
            # OUT: True(tradeable) / False(not tradeable)

        try:
            # asset =  get asset from alpaca wrapper (.tradeable)
            if not asset.tradeable:
                lg.info(' The asset %s is not tradeable' % ticker)
                return False
            else:
                lg.info('The asset %s is tradeable!' % ticker)
                return True

        except:
            lg.error('The asset %s is not answering well' % ticker)
            return False

    def set_stoploss(self,entryPrice,direction):

    # takes an entry price as a input and sets the stoploss (direction)
                # IN: entry price, direction (long/short)
                # OUT:stoploss

        stopLossMargin = 0.05 # percentage margin

        try:
            if direction == 'long':
                # example 10 - (10*0.05) = 9.5
                stopLoss = entryPrice - (entryPrice * stopLossMargin)
                return stopLoss

            elif direction == 'short':
                # example 10 + (10*0.05) = 10.5

                stopLoss = entryPrice + (entryPrice * stopLossMargin)
                return stopLoss

            else:
                raise ValueError

        except Exception as e:
            lg.error('The direction value is not understood: %s' % str(direction))
            sys.exit()

    def set_takeprofit(self,entryPrice,direction):

        # set take profit: takes a price as an input and sets the takeprofit
            # IN: entry price,direction (long/short)
            # OUT: take takeprofit

        takeProfitMargin = 0.1 # percentage margin

        try:
            if direction == 'long':
                # example 10 + (10*0.1) = 11
                takeProfit = entryPrice + (entryPrice * takeProfitMargin)
                return takeProfit

            elif direction == 'short':
                # example 10 - (10*0.1) = 9
                takeProfit = entryPrice - (entryPrice * takeProfitMargin)
                return takeProfit

            else:
                raise ValueError

        except Exception as e:
            lg.error('The direction value is not understood: %s' % str(direction))
            sys.exit()

    # load historical stock data:
        # IN: ticker, interval, entries limit
        # OUTL array with stock data(OHCL)

    def get_open_poisitions(self,assetId):
        # get open posiitons
            # IN: assetId (unique identifier)
            # OUT: boolean( True = already open, False = not open)

        # posiitons = ask alpaca wrapper for the list of open positions
        for position in positions:
            if position.symbol == assetId:
                return True

            else:
                return False




    # submit order: gets our order through the API (retry)
        # IN: order data, order type
        # OUT: boolean (True = order went through, False = order did not)

    # cancel order: cancels our order (retry)
        # IN: order id
        # OUT: boolean (True = order cancelled, False = order not cancelled)

    def check_position(self,assset):

        # check position: check whether the position exists or not
          # IN: ticker
          # OUT: boolean (True = order is there, False = order not there)
          maxAttempts = 5
          attempt = 1

          while attempt < maxAttempts:
            try:
                    # position = ask the alpaca wrapper for a position
                currentPrice = position.current_price
                lg.info('The position was checked. Current price is: %.2f' % currentPrice)
                return True
            except:
                lg.info('Position not found, waiting for it...')
                time.sleep(5) # wait 5 seconds and retry
                attempt += 1

           lg.info('Position not found for %s, not waiting any more' % asset)
           return False


    def get_general_trend(self,asset):

    # get general trend: detect interseting trend (UP / DOWN / NO TREND)
        # IN: asset
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
                        lg.info('Trend detected for %s: long' % asset)
                        return 'long'
                    # elif (ema50 < ema26) and (ema50 < ema9):
                        lg.info('Trend detected for %s: short' % asset)
                        return 'short'
                    # elif attempts <= maxAttempts:
                        lg.info('Trend not clear for %s, waiting...' % asset)
                        attemp += 1
                        time.sleep(60)
                    # else:
                        lg.info('Trend NOT detected for %s' % asset)
                        return 'no trend'

         except Exception as e:
             lg.error('Something went wrong at get general trend')
             lg.error(e)
             sys.exit()


    def  get_insant_trend(self,asset,trend):

        # get instant trend: confirm the trend detected by GT analysis
            # IN: asset, trend (long / short)
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

                lg.info('%s instant trend EMAs: [%.2f,%.2f,%.2f]' % (asset,ema9, ema26, ema50))


                if (trend== 'long') and (ema9 > ema26) and (ema26 > ema50):
                    lg.info('Long trend confirmed for %s' % asset)
                    return True
                elif (trend == 'short') and (ema9 < ema26) and (ema26 < ema50):
                    lg.info('Short trend confirmed for %s' % asset)
                    return True
                elif attempt <= maxAttempts:
                    lg.info('Trend not clear for %s, waiting...' % asset)
                    attemp += 1
                    time.sleep(30)
                else:
                    lg.info('Trend NOT detected for %s' % asset)
                    return False

        except Exception as e:
            lg.error('Something went wrong at get instant trend')
            lg.error(e)
            sys.exit()


    def get_rsi(self,asset,trend):

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


                    lg.info('%s rsi = [%.2f]' % (asset,rsi))


                    if (trend== 'long') and (rsi > 50) and (rsi < 80):
                        lg.info('Long trend confirmed for %s' % asset)
                        return True
                    elif (trend == 'short') and (rsi < 50) and (rsi > 20):
                        lg.info('Short trend confirmed for %s' % asset)
                        return True
                    elif attempt <= maxAttempts:
                        lg.info('Trend not clear for %s, waiting...' % asset)
                        attemp += 1
                        time.sleep(20)
                    else:
                        lg.info('Trend NOT detected for %s' % asset)
                        return False

            except Exception as e:
                lg.error('Something went wrong at rsi analysis')
                lg.error(e)
                sys.exit()

            

    def get_stochastic(self,asset,trend):

        # get stochastic: perform STOCHASTIC analysis
            # IN: asset, trend
            # OUT: True(confirmed) / False(not confirmed)

        lg.info('STOCHASTIC ANALYSIS entered')

        attempt = 1
        maxAttempts = 20 # total time = maxAttempts * 10s (as implemented)

        try:
            while True:
                # data = ask Alpaca wrapper for 5 min candles

                # calculate the STOCHASTIC
                stoch_k, stoch_d = ti.stoch(high, low, close, 9, 6, 9)



                lg.info('%s stochastic = [%.2f,%.2f]' % (asset,stoch_k,stoch_d))


                if (trend== 'long') and (stoch_k > stoch_d) and (stoch_k < 80) and (stoch_d < 80):
                    lg.info('Long trend confirmed for %s' % asset)
                    return True
                elif (trend == 'short') and (stoch_k < stoch_d) and (stoch_k > 20) and (stoch_d < 20):
                    lg.info('Short trend confirmed for %s' % asset)
                    return True
                elif attempt <= maxAttempts:
                    lg.info('Trend not clear for %s, waiting...' % asset)
                    attemp += 1
                    time.sleep(10)
                else:
                    lg.info('Trend NOT detected for %s' % asset)
                    return False

        except Exception as e:
            lg.error('Something went wrong at stochastic analysis')
            lg.error(e)
            sys.exit()


    # enter position mode: check the conditions in parallel once inside the position
        # IF check take profit. If True -> close position
            # IN: current gains (earning $)
            # OUT: True / False

        # ELIF check stop loss. If True -> close position
            # IN: current gains (loosing $)
            # OUT: True / False

        # ELIF check stoch crossing. Pull OHLC data. If True -> close position
            # STEP 1: pull 5 minutes  OHLC data.
                # IN: asset
                # OUT: OHLC data (5 min candles)
            # STEP 2: see whether the stochastic curves are crossing
                # IN: OHLC data (5 min candles)
                # OUT: True / False





    def run():



        #LOOP until timeout reached (ex. 2h)

        #POINT ECHO: INITIAL CHECK
        # check the position: ask the broker/API if we have an open position with asset
            # IN: asset (string)
            # OUT: True(exists) / False(does not exist)

        # POINT DELTA
        #get general trend: find a trend
            #LOOP until timeout reached (Ex. 30 minutes)

        # get instant trend
            # if failed go back to POINT DELTA

        # perform RSI  analysis
            # if failed go back to POINT DELTA

        # perform STOCHASTIC analysis
            # if failed go back to POINT DELTA

        # submit order(limit)
            # if false, abort / go back to point ECHO

        # check position
            # if False, abort / go back to POINT ECHO

        # enter position mode

        #GET OUT
        # submit order(market)
            # if false, retry until it works

        # check position: see if the position exists
            # if False, abort / go back to SUBMIT ORDER

        # wait 15 min

        # end
