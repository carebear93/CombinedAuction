# Library
import random
import csv
import termcolor
import colorama
import datetime
import time
import decimal

# Library Module
from colorama import Fore
from colorama import init
from termcolor import colored
from numpy import genfromtxt
from datetime import datetime, timedelta

# Class import
from auction import *
from bidderAgent import bidderAgent
from varibles import varibles

"""
Made by Kristian Care 14/04/2019 | University of Aberdeen
"""

class Main:
    #############################################
    #############################################
    ##############Import Varibles################
    a = bidderAgent()
    e = Auction()
    v = varibles()
    ##############Import Varibles################
    #############################################
    #############################################

    """
    Please see globalVarible.py for varibles & descriptions
    """

    # Welcome the user
    e.introduction()

    # Set starting price!
    e.setPrice()

    # Generate ticket
    e.cast_ticketInfo()

    # Ask user to confirm they are happy with the parameters
    # If yes, begin auction, else, exit program
    answer = raw_input("Being the auction?: [y/n]: ")
    print (type(answer))
    if not answer or answer[0].lower() != 'y':
        print("You did not indicate approval")
        exit(1)
    else:
        a.setBudget()
        print ("Agent budget set to:", Budget)
        e.englishAuction()
