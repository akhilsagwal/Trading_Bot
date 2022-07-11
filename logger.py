#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging as lg
import os
from datetime import datetime

def initialize_logger():

    # creaiting a folder for the logs
    logs_path='./logs/'
    try:
        os.mkdir(logs_path)
    except OSError:
             print("Creation of the directory %s failed - it does not have to be bad"% logs_path)
    else:
        print("Succesfully created log directory")

    # renaming each log depending on the time
    date=datetime.now().strftime("%Y%m%d_%H%M%S")
    log_name=date + '.log'
    currentLog_path=logs_path + log_name

    # log parameters
    lg.basicConfig(filename=currentLog_path,format='%(asctime)s-%(levelname)s: %(message)s', level=lg.DEBUG)
    lg.getLogger().addHandler(lg.StreamHandler())

    # init message
    lg.info('Log initialized')
