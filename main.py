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
from auction import english_auction
from globalVarible import initialPrice, Location, Destination, ticket_id, RESERVE_RATE
from bidderAgent import bidderAgent

"""
Made by Kristian Care 14/04/2019 | University of Aberdeen
"""

class Main:
    #############################################
    #############################################
    ##############Import Varibles################
    a = bidderAgent()
    e = english_auction()
    ##############Import Varibles################
    #############################################
    #############################################

    """
    Please see globalVarible.py for varibles & descriptions
    """

    # Welcome message
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
    def cast_ticketInfo(id, loc, des, init, res):
        print ("")
        print ("#####TICKET TO BE AUCTIONED#####")
        print ("   Ticket ID: ", id)
        print ("   Ticket Location: ", loc)
        print ("   Ticket Destiantion: ", des)
        print ("   Starting Price: ", init)
        print ("   Reserve Price: ", res)
        print ("#####TICKET TO BE AUCTIONED#####")
        print ("")

    # Welcome
    introduction()
    # Set Initial Price
    initialPrice = int(input("Please set the initial price: "))
    # Set Reserve Price from Initial Price
    global reservePrice
    reservePrice = initialPrice * RESERVE_RATE
    # Generate Ticket
    cast_ticketInfo(ticket_id, Location, Destination, initialPrice, reservePrice)
    # Allow user to check confirm they are happy with the ticket
    global answer
    answer = input("Being the auction?: [y/n]: ")
    # If yes begin auction, else exit program
    if not answer or answer[0].lower() != 'y':
        print("You did not indicate approval")
        exit(1)
    else:
        a.set_Budget()
        e.englishAuction()
