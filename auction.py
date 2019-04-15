# Import Library
import random
import csv
import pandas as pd
import numpy as np
import termcolor
import colorama
import time
import decimal

# Class Import
from globalVarible import *
from bidderAgent import *

g = globalVarible()
b = bidderAgent()

class english_auction:

    ###################################
    #             AUCTION             #
    ###################################

    # Timer for 20 seconds
    def timer():
        run = input("Start? > ")
        mins = 0
        # Only run if the user types in "start"
        if run == "start":
            # Loop until we reach 20 seconds running
            while mins != 20:
                print (">>>>>>>>>>>>>>>>>>>>>", mins)
                # Sleep for a minute
                time.sleep(1)
                # Increment the minute total
                mins += 1

    # Function to check for a winner!
    # If there is only 1 bidder they win!

    def englishAuction():
        print ("Auctioneer: OPEN-CRY! ", ticket_id, "starting price at ", startingPrice)
        # While there is no winner for the auction
        while currentBid == 1:
            if auctionWinner == False:
                # New round!
                global auctionRound
                auctionRound += 1
                # Announce round and allow bids!
                print ("Auctioneer: Round ", auctionRound,"place your bids!")
                # Agent makes bid if within budget
                b.bid()
                # Initate round timer
                run = auctionWinner
                mins = 0
                # Only run if the user types in "start"
                if run == False:
                    # Loop until we reach 20 seconds running
                    while mins != 10:
                        print (">>>>>>>>>>>>>>>>>>>>>", mins)
                        # Sleep for a minute
                        time.sleep(1)
                        # Increment the minute total
                        mins += 1
                if currentBid == 1:
                    increasePrice + startingPrice
                #ea.checkForWinner()
            else:
                print ("The auction has concluded!")

    englishAuction()
