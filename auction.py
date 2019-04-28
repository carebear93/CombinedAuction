# Import Library
import random
import csv
import termcolor
import colorama
import time
import decimal

# Class Import
from bidderAgent import *
from varibles import varibles

b = bidderAgent()
v = varibles()

"""
Made by Kristian Care 14/04/2019 | University of Aberdeen
"""
with open('towns.csv', 'r') as csvfile:
    towns = list(csv.reader(csvfile))

###################################
#             AUCTION             #
###################################

########### TICKET VARIBLES ##########
# Reserve Rate
RESERVE_RATE = 0.4

# Set Reserve Price
reservePrice = v.initialPrice / RESERVE_RATE

# Ticket ID
ticket_id = random.randint(1,101)

# Starting Location of Train Ticket
Location = (random.choice(towns))

# Destination of Train Ticket
Destination = (random.choice(towns))

##########  AUCTION VARIBLES ##########

# Auction Round
auctionRound = 0

# Auction winner
auctionWinner = False

# Increase Offer
increasePrice = v.initialPrice / 3

# Decrease Offer
decreasePrice = v.initialPrice / 6
############################################################################

class Auction:


    # Welcome to Jurassic Park!
    def introduction(self):
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

    # Set inital price
    def setPrice(self):
        v.change(int(input("Please set the initial price: ")))

    # Function to announce to ticket to be AUCTIONED
    def cast_ticketInfo(self):
        print ("")
        print ("#####TICKET TO BE AUCTIONED#####")
        print ("   Ticket ID: ", ticket_id)
        print ("   Ticket Location: ", Location)
        print ("   Ticket Destiantion: ", Destination)
        print ("   Starting Price: ", v.initialPrice)
        print ("   Reserve Price: ", reservePrice)
        print ("#####TICKET TO BE AUCTIONED#####")
        print ("")

    def englishAuction(self):
        global auctionRound
        print ("<English Auction>")
        print ("Auctioneer: OPEN-CRY! ticket ID: ", ticket_id, "starting price at ", v.initialPrice)
        # While there is no winner for the auction
        while currentBid == 1:
            if auctionWinner == False:
                # New round!
                auctionRound += 1
                # Announce round and allow bids!
                print ("Auctioneer: Round ", auctionRound,"do I have", v.initialPrice,"?")
                # Agent msakes bid if within budget
                b.bid()
                # Initate round timer
                run = auctionWinner
                mins = 0
                # Only run if the user types in "start"
                if run == False:
                    # Loop until we reach 4 seconds running
                    while mins !=4:
                        print (">>>>>>>>>>>>>>>>>>>>>", mins)
                        # Sleep for a minute
                        time.sleep(1)
                        # Increment the minute total
                        mins += 1
                if currentBid == 1:
                    increasePrice + v.initialPrice
                #ea.checkForWinner()
            else:
                print ("The auction has concluded!")

        def dutchAuction(self):
            global auctionRound
            print ("<Dutch Auction>")
            print ("Auctioneer: OPEN-CRY! ", ticket_id, "starting price at ", v.initialPrice)
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
                        # Loop until we reach 4 seconds running
                        while mins !=4:
                            print (">>>>>>>>>>>>>>>>>>>>>", mins)
                            # Sleep for a minute
                            time.sleep(1)
                            # Increment the minute total
                            mins += 1
                    if currentBid == 1:
                        decreasePrice - v.initialPrice
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
