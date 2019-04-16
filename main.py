# Library
import random
import csv
import pandas as pd
import numpy as np
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
from hello import *
from auction import english_auction
from globalVarible import initialPrice, Location, Destination, ticket_id
from bidderAgent import bidderAgent

"""
Made by Kristian Care 14/04/2019 | University of Aberdeen
"""
class Main:
    #############################################
    #############################################
    ##############Import Varibles################
    a = bidderAgent()
    g = globalVarible()
    h = hello()
    e = english_auction()
    ##############Import Varibles################
    #############################################
    #############################################

    """
    Please see globalVarible.py for varibles & descriptions
    """
    def introduction():
        print ("##########################################")
        print ("")
        print ("Welcome to the combined auction system!")
        print ("This program asks you to pick an intial price to begin an english auction.")
        print ("From this, a reserve price is set, and both prices are assigned to a random train ticket...")
        print ("Once you are happy with the parameters the auction will begin...")
        print ("Enjoy!")
        print ("")
        print ("##########################################")
        print ("")
        print ("")

    # Function to announce to ticket to be AUCTIONED
    def cast_ticketInfo():
        print ("")
        print ("#####TICKET TO BE AUCTIONED#####")
        print ("   Ticket ID: ", ticket_id)
        print ("   Ticket Location: ", Location)
        print ("   Ticket Destiantion: ", Destination)
        print ("   Starting Price: ", initialPrice)
        print ("   Reserve Price: ", reservePrice)
        print ("#####TICKET TO BE AUCTIONED#####")
        print ("")

    introduction()
    initialPrice = int(input("Please set the initial price: "))
    cast_ticketInfo()
    answer = input("Being the auction?: [y/n]: ")
    if not answer or answer[0].lower() != 'y':
        print("You did not indicate approval")
        exit(1)
    else:
        a.set_Budget()
        e.englishAuction()
