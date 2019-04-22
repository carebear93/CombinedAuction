# Import Library
import random
import csv
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

    def englishAuction(self):
        global auctionRound
        print ("<English Auction>")
        print ("Auctioneer: OPEN-CRY! ", ticket_id, "starting price at ", initialPrice)
        # While there is no winner for the auction
        while currentBid == 1:
            if auctionWinner == False:
                # New round!
                auctionRound += 1
                # Announce round and allow bids!
                print ("Auctioneer: Round ", auctionRound,"do I have", initialPrice,"?")
                # Agent msakes bid if within budget
                b.bid()
                # Initate round timer
                run = auctionWinner
                mins = 0
                # Only run if the user types in "start"
                if run == False:
                    # Loop until we reach 20 seconds running
                    while mins !=4:
                        print (">>>>>>>>>>>>>>>>>>>>>", mins)
                        # Sleep for a minute
                        time.sleep(1)
                        # Increment the minute total
                        mins += 1
                if currentBid == 1:
                    increasePrice + initialPrice
                #ea.checkForWinner()
            else:
                print ("The auction has concluded!")

        def dutchAuction(self):
            global auctionRound
            print ("<Dutch Auction>")
            print ("Auctioneer: OPEN-CRY! ", ticket_id, "starting price at ", initialPrice)
            # While there is no winner for the auction
            while currentBid == 1:
                if auctionWinner == False:
                    # New round!
                    auctionRound += 1
                    # Announce round and allow bids!
                    print ("Auctioneer: Round ", auctionRound,"place your bids!")
                    # Agent msakes bid if within budget
                    b.bid()
                    # Initate round timer
                    run = auctionWinner
                    mins = 0
                    # Only run if the user types in "start"
                    if run == False:
                        # Loop until we reach 20 seconds running
                        while mins !=4:
                            print (">>>>>>>>>>>>>>>>>>>>>", mins)
                            # Sleep for a minute
                            time.sleep(1)
                            # Increment the minute total
                            mins += 1
                    if currentBid == 1:
                        increasePrice - decreasePrice
                    #ea.checkForWinner()
                else:
                    print ("The auction has concluded!")

            # Timer for 20 seconds
            def timer():
                run1 = answer
                mins = 0
                # Only run if the user types in "start"
                if run1 == "y":
                    # Loop until we reach 20 seconds running
                    while mins != 8:
                        print (">>>>>>>>>>>>>>>>>>>>>", mins)
                        # Sleep for a minute
                        time.sleep(1)
                        # Increment the minute total
                        mins += 1
