import random
import csv
import pandas as pd
import numpy as np
import termcolor
import colorama

from colorama import Fore
from colorama import init
from termcolor import colored
from hello import introduction
from numpy import genfromtxt

#############################################
#############################################
RESERVE_RATE = 0.4

#towns = np.genfromtxt ('towns.csv', delimiter=",")
with open('towns.csv', 'rb') as csvfile:
    towns = list(csv.reader(csvfile))

# Ticket varibles
Location = (random.choice(towns))
Destination = (random.choice(towns))
#############################################
#############################################
introduction()

print (Fore.YELLOW + "Auctioneer: Welcome to the Auction!")

# User sets intial price of the ticket
initialPrice = input("Auctioneer: Set initial price: ")

# Reserve price determined from the intial price
reservePrice = initialPrice * RESERVE_RATE
print ("Auctioneer: Reserve price set at", reservePrice)

# Generated tickets are stored in an Create generateTicket Function
def generateTicket():
    print (" ")
    print ("##########Ticket to be Auctioned!##########")
    ticket = ["ID:",random.randint(1,99), "Location", Location, "Destination", Destination, "Starting Price:", initialPrice, "Reserve Price", reservePrice]
    print (ticket)

generateTicket()
