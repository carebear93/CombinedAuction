# Library
import random
import csv
import termcolor
import colorama
import datetime
import time
import decimal

# Import Class
from globalVarible import *
from threading import Thread

g = globalVarible()

"""
Made by Kristian Care 14/04/2019 | University of Aberdeen
"""

#class bidderAgent(Thread):
class bidderAgent:

    """__init__() functions as the class constructor"""

    """
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname
    """

    def set_Budget(self):
        # Set Agents Budget
        Budget = initialPrice * random.randint(155, 389)/100
        print ("Budget for the Agent: ", Budget)

    def bid(self):
        # Bid function
        global amountOfBids
        if Budget <= initialPrice:
            currentBid = 1
            if currentBid == 1:
                amountOfBids += 1
            print (" ")
            print ("Participant: I will bid this round!")
            print (" ")
        else:
            currentBid = 0
            if currentBid == 0:
                amountOfBids -=1
            ("is out!")
