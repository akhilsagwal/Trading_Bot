# encoding: utf-8

# import needed libraries
from traderlib import *
from logger import *
import sys


import alpaca_trade_api as tradeapi


import gvars


# check our trading account (blocked? total amount?)
def check_account_ok(api):
    try:

        account = api.get_account()
        if account.status != 'ACTIVE':
            lg.error('The account is not ACTIVE, aborting')
            sys.exit()

    except Exception as e:
        lg.error('Could not get account info')
        lg.info(str(e))
        sys.exit()

# close current orders (doublecheck)
def clean_open_orders(api):

    lg.info('Cancelling all orders...')

    try:
        api.cancel_all_orders()
        lg.info('All orders cancelled')
    except Exception as e:
        lg.error('Could not cancel all orders')
        lg.error(e)
        sys.exit()


# execute trading bot
def main():

    api = tradeapi.REST(gvars.API_KEY, gvars.API_SECRET_KEY, gvars.API_URL)


    # OUT: boolean tradingSuccess (True = success / False = failure)

    # initialize the logger (imported from logger)
    initialize_logger()

    # check our trading account
    check_account_ok(api)

    # close current orders
    clean_open_orders(api)
    import pdb; pdb.set_trace()
    # get ticker
    ticker = input('Write the ticker you want to operate with: ')


    trader = Trader(ticker) # initialize trading bot
    tradingSuccess = trader.run() # run trading bot library

    if not tradingSuccess:
        lg.info('Trading was not successful, locking asset')
        # wait whatever time






if __name__ == '__main__':
    main()
