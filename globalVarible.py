# Import Library
import random
import csv
import pandas as pd
import numpy as np
import termcolor
import colorama
import time
import decimal

with open('towns.csv', 'r') as csvfile:
    towns = list(csv.reader(csvfile))

class globalVarible:
    """
    This file sets important global varibles.
    I kept having problems with circular imports.
    These varibles are are stored called away from this file.
    All varibles here are set to global.
    """

    ########### TICKET VARIBLES ##########
    # Reserve Rate
    global RESERVE_RATE
    RESERVE_RATE = 0.4

    # User sets intial price of the ticket
    #initialPrice = int(input("Please set the initial price: "))

    # Ticket Starting Price
    global startingPrice
    startingPrice = 100

    # Ticket ID
    global ticket_id
    ticket_id = random.randint(1,101)

    # Starting Location of Train Ticket
    global Location
    Location = (random.choice(towns))

    # Destination of Train Ticket
    global Destination
    Destination = (random.choice(towns))

    ##########  AUCTION VARIBLES ##########
    # Agent Budget
    global Budget
    Budget = 0

    # Agent current bid
    global currentBid
    currentBid = 1

    # Auction Round
    global auctionRound
    auctionRound = 0

    # Auction winner
    global auctionWinner
    auctionWinner = False

    # Increase Offer
    global increasePrice
    increasePrice = startingPrice / 5

    # Amount of bids
    global amountOfBids
    amountOfBids = 0
