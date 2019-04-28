# Library
import random
import csv
import termcolor
import colorama
import datetime
import time
import decimal

from varibles import varibles
"""
Made by Kristian Care 14/04/2019 | University of Aberdeen
"""

v = varibles()

Budget = 0
amountOfBids = 0
currentBid = 1

#class bidderAgent(Thread):
class bidderAgent:

    # TODO: Turn class into list to have multiple bidders!

    """__init__() functions as the class constructor"""

    """
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname
    """
    """global Budget
    Budget = 0

    # Agent current bid
    global currentBid
    currentBid = 1

    # Amount of bids
    global amountOfBids
    amountOfBids = 0"""
    def setBudget(self):
        global Budget
        Budget = v.initialPrice * random.randint(155, 389)/100

    def bid(self):
        global amountOfBids
        global currentBid
        global Budget
        if Budget <= v.initialPrice:
            currentBid = 1
            if currentBid == 1:
                amountOfBids += 1
            print (" ")
            print ("Agent: I shall bid this round!")
            print (" ")
        else:
            currentBid = 0
            if currentBid == 0:
                amountOfBids -=1
            ("is out!")
