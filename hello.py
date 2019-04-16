# Import Library
import random
import csv
import pandas as pd
import numpy as np
import termcolor
import colorama
import time
import decimal

# Class import
from globalVarible import *

g = globalVarible()

class hello:

    # import class varible
    g = globalVarible()

    # Reserve price determined from the intial price
    global reservePrice
    reservePrice = initialPrice * RESERVE_RATE
    print ("Reserve price set at", reservePrice)
