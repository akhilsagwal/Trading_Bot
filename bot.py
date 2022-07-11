# encoding: utf-8

# import needed libraries
from traderlib import *
from logger import *
import sys

# initialize the logger
initialize_logger()

# check our trading account (blocked? total amount?)
def check_account_ok():
    try:
        #get account info
    except Exception as e:
        lg.error('Could not get account info')
        lg.info(str(e))
        sys.exit()

# close current orders (doublecheck)
def clean_open_order():
    # get list of open orders
    lg.info('List of open orders')
    lg.info(str(open_orders))

    for order in open_order:
        #close orders
        lg.info('Order %s closed' % str(order.id))

    lg.info('Closing orders complete')


# define asset
def get_ticker():
    # enter ticker with the keyboard
    ticker = input('Write the ticker you want to operate with: ')

    return ticker




# execute trading bot
def main():

    # initialize the logger
    initialize_logger()

    # check our trading account
    check_account_ok()
    
    # close current orders
    clean_open_order():

    # define asset
    ticker = get_ticker()

    # run trading bot
        # IN: string (ticker)
        # OUT: boolean (True = success / False = failure)

if __name__ == '__main__':
    main()
