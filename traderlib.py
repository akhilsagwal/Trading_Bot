
#LOOP until timeout reached (ex. 2h)
#POINT ECHO: INITIAL CHECK
# check the position: ask the broker/API if we have an open position with asset
    # IN: asset (string)
    # OUT: True(exists) / False(does not exist)

#check if tradeable: ask the broker/API if "asset" is tradeable
    # IN: asset (string)
    # OUT: True(exists) / False(does not exist)

#GENERAL TREND
# load 30 min candles: demand the API the 30 min candles
    # IN : asset(or whatever the API needs), time range*,candle size*
    # OUT: 30 min candles(OHLC for every candle)

#perform general trend analysis: detect interesting trend( UP / DOWN / NO TREND )
    # IN: 30 min candles data (Closed data)
    # OUT: UP / DOWN / NO TREND (strings)
    #if no trend defined, go back to POINT ECHO

    #LOOP until timeout reached (Ex. 30 minutes)
    # POINT DELTA
    # STEP 1 : load 5 min candles
        # IN : asset(or whatever the API needs), time range*,candle size*
        # OUT: 5 min candles(OHLC for every candle)
        # if failed go back to POINT DELTA

    # STEP 2 : perform instant trend analysis: confirm the trend detected by GT analysis
        # IN: 5 min candles data (Closed data), output of the GT analysis(UP / DOWN string)
        # OUT: True(confirmed) / False(not confirmed)
        # if failed go back to POINT DELTA

    #  STEP 3 : perform RSI  analysis
        # IN: 5 min candles data (Closed data), output of the GT analysis(UP / DOWN string)
        # OUT: True(confirmed) / False(not confirmed)
        # if failed go back to POINT DELTA

    # STEP 4 : perform stochastic analysis
        # IN: 5 min candles data (OHLC data), output of the GT analysis(UP / DOWN string)
        # OUT: True(confirmed) / False(not confirmed)
        # if failed go back to POINT DELTA

#SUBMIT ORDER
# submit order(limit) : interact with broker API
    # IN: # of shares to operate with,asset, desired price
    # OUT: True (confirmed) / False (not confirmed), position ID
    # if false, abort / go back to point ECHO

# check position: see if the position exists
    # IN: position ID
    # OUT: True (confirmed) / False (not confirmed)
    # if False, abort / go back to POINT ECHO

#LOOP until timeout reached (ex. ~8h)
#ENTER POSITION MODE: check the conditions in parallel
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
    # STEP 2: see whether the stochastc curves are crossing
        # IN: OHLC data (5 min candles)
        # OUT: True / False

#GET OUT
#SUBMIT ORDER
# submit order(market): interact with broker API
    # IN: # of shares to operate with,asset, position ID
    # OUT: True (confirmed) / False (not confirmed)
    # if false, retry until it works

# check position: see if the position exists
    # IN: position ID
    # OUT: True (still exists!) / False (does not exist)
    # if False, abort / go back to SUBMIT ORDER

# wait 15 min

# end
