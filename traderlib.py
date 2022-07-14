# encoding: utf-8
import sys


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

    # check position: check whether the position exists or not
      # IN: ticker
      # OUT: boolean (True = order is there, False = order not there)

    # get general trend: detect interseting trend (UP / DOWN / NO TREND)
        # IN: 30 min candles data (Close data)
        # OUTPUT: UP / DOWN / NO TREND (strings)
        #If no trend defined, go back to POINT ECHO

    # get instant trend: confirm the trend detected by GT analysis
        # IN: 5 min candles data (Closed data), output of the GT analysis(UP / DOWN string)
        # OUT: True(confirmed) / False(not confirmed)
        # if failed go back to POINT DELTA

    # get rsi: perform RSI analysis
        # IN: 5 min candles data (Closed data), output of the GT analysis(UP / DOWN string)
        # OUT: True(confirmed) / False(not confirmed)
        # if failed go back to POINT DELTA

    # get stochastic: perform STOCHASTIC analysis
        # IN: 5 min candles data (OHLC data), output of the GT analysis(UP / DOWN string)
        # OUT: True(confirmed) / False(not confirmed)
        # if failed go back to POINT DELTA

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


        # load historical data: demand the API the 30 min candles

        #get general trend

            #LOOP until timeout reached (Ex. 30 minutes)
            # POINT DELTA
            # STEP 1 : load historical data: demand the API the 30 min candles
                # if failed go back to POINT DELTA

            # STEP 2 : get instant trend


            #  STEP 3 : perform RSI  analysis


            # STEP 4 : perform STOCHASTIC analysis


        #SUBMIT ORDER
        # submit order(limit)
            # if false, abort / go back to point ECHO

        # check position
            # if False, abort / go back to POINT ECHO

        #LOOP until timeout reached (ex. ~8h)
        # enter position mode


        #GET OUT

        # submit order(market)
            # if false, retry until it works

        # check position: see if the position exists
            # if False, abort / go back to SUBMIT ORDER

        # wait 15 min

        # end
