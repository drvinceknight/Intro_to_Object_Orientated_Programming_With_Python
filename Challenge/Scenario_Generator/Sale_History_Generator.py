#! /usr/bin/env python
from math import exp
import csv
import os
import random
import sys
"""
This file generates a data file to be used as the Sales History for the challenge. The code generates a number of customers for each day (the total number of days is an input parameter) sampled from a Poisson distribution.

Each customer has various attributes including how likely they are to buy products and if they are likely to sign up to the loyalty programme. A dictionary is generated for each customer that gives their probability of buying a product from each department.

One can input the name of the file to be produced (Default: "Sale_History.csv").
"""

#Uncomment if you want to stick to a random seed (ie recreate same Sales History again and again).
#random.seed(1)


def poisson_sample(lmbda):
    """
    An algorithm of Knuth to sample numbers from a Poisson distribution.
    """
    L, k, p = exp(-lmbda), 0, 1
    while p > L:
        p *= random.random()
        k += 1
    return k - 1


def import_file(stock_report="Stock_Report.csv"):
    """
    A function to import a Stock Report file. It returns a dictionary with keys the departments and values the list of available products.
    """
    outfile = open(stock_report, "rb")
    data = csv.reader(outfile)
    data = [row for row in data]
    outfile.close()
    P = {}
    for row in data[1:]:
        if row[0] in P:
            P[row[0]].append(row[1])
        else:
            P[row[0]] = [row[1]]
    return P


class Customer():
    """
    This class defines a customer with various attributes:

    - A dictionary that defines how likely the customer is to buy a product from each department.
    - A basket (with products bought using the above dictionary).
    - Whether or not the customer signs up to the loyalty scheme.

    This class has a method "new_basket" which regenerates a basket if needed.
    """
    def __init__(self, products, buying_probability=.8, loyal_probability=.5):
        #Create a dictionary that will contain the buying probability for each department for this customer.
        self.buying_prob = {}
        for e in products:
            dep_buying_prob = buying_probability * random.random()
            temp_dict = {}
            for i in products[e]:
                temp_dict[i] = random.random() * dep_buying_prob
            self.buying_prob[e] = temp_dict

        self.basket = []
        for e in products:
            for i in products[e]:
                if random.random() < self.buying_prob[e][i]:
                    self.basket.append(i)

        self.loyal = False
        if random.random() < loyal_probability:
            self.loyal = True

    def new_basket(self, products):
        self.basket = []
        for e in products:
            for i in products[e]:
                if random.random() < self.buying_prob[e][i]:
                    self.basket.append(i)


class Sale_History():
    """
    Class for the Sale History. On initialisation it creates customers for each day of sale (the number of customers is randomly sampled from the Poisson distribution). There is a method "create_file" that outputs a csv file.
    """
    def __init__(self, products, mean_customers_per_day, days, returning_loyal_customer_prob=.6):
        self.days = days
        #Initialise the data file to be output:
        self.data = [["Date", "Loyalty Number (0 = Not on scheme)", "Basket"]]
        #A list of loyal customers:
        loyal_customers = []
        for i in range(self.days):
            #Sample number of customers that day:
            customers = poisson_sample(mean_customers_per_day)
            for e in range(customers):
                #Check whether customer is a returning loyal customer:
                if len(loyal_customers) > 0 and random.random() < returning_loyal_customer_prob:
                    #Pick random customer from loyal_customers:
                    cust = random.choice(loyal_customers)
                    #Generate new basket for customer:
                    cust.new_basket(products)
                    loyalty_number = id(cust)
                else:
                    #If customer is not a returning customer generate a new one:
                    cust = Customer(products)
                    #Check if new customer signs up to loyalty scheme:
                    if cust.loyal:
                        loyal_customers.append(cust)
                    loyalty_number = 0
                self.data.append([i + 1, loyalty_number, cust.basket])

    def create_file(self, filename="Sale_History.csv"):
        #Write Sale_History file.
        outfile = open(filename, "wb")
        output = csv.writer(outfile)
        for row in self.data:
            output.writerow(row)
        outfile.close()
        print "---------------------"
        print ""
        print "Output file: %s created with %s baskets over %s days:" % (filename, len(self.data) - 1, self.days)
        print ""
        print "---------------------"

"""
The above classes need a Stock Report as input. The following code imports "Stock_Report.csv" as default if no file name is passed at the command line.
"""
files_in_directory = os.listdir(".")

if len(sys.argv) == 1:
    if "Stock_Report.csv" not in files_in_directory:
        print "-----"
        print ""
        print "No Stock Report file found."
        print ""
        print "-----"
    else:
        stock_report = "Stock_Report.csv"
else:
    stock_report = sys.argv[1]

products = import_file(stock_report)
a = Sale_History(products, 1000, 30)
a.create_file()
