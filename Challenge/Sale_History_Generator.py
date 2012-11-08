#! /usr/bin/env python
import random
import sys
import csv
import os
from math import exp

#random.seed(1)

files_in_directory=os.listdir(".")

def poisson_sample(lmbda):
    L,k,p=exp(-lmbda),0,1
    while p>L:
        p*=random.random()
        k+=1
    return k-1


def import_file(Stock_Report="Stock_Report.csv"):
    outfile=open(Stock_Report,"rb")
    data=csv.reader(outfile)
    data=[row for row in data]
    outfile.close()
    P={}
    for row in data[1:]:
        if row[0] in P:
            P[row[0]].append(row[1])
        else:
            P[row[0]]=[row[1]]
    return P

class Customer():
    def __init__(self,Products,buying_probability=.8,Loyal_probability=.5):
        buying_prob={}
        for e in Products:
            dep_buying_prob=buying_probability*random.random()
            temp_dict={}
            for i in Products[e]:
                temp_dict[i]=random.random()*dep_buying_prob
            buying_prob[e]=temp_dict
        self.buying_prob=buying_prob

        basket=[]
        for e in Products:
            for i in Products[e]:
                if random.random()<self.buying_prob[e][i]:
                    basket.append(i)
        self.basket=basket

        self.loyal=False
        if random.random()<Loyal_probability:
            self.loyal=True

    def new_basket(self,Products):
        basket=[]
        for e in Products:
            for i in Products[e]:
                if random.random()<self.buying_prob[e][i]:
                    basket.append(i)
        self.basket=basket




class Sale_History():
    def __init__(self,Products,Mean_Customers_Per_Day,Days,returning_loyal_customer_prob=.6):
        self.Days=Days
        data=[["Date","Loyalty Number (0=Not on scheme)","Basket"]]
        loyal_customers=[]
        for i in range(Days):
            customers=poisson_sample(Mean_Customers_Per_Day)
            for e in range(customers):
                if len(loyal_customers)>0 and random.random()<returning_loyal_customer_prob:
                    cust=random.choice(loyal_customers)
                    cust.new_basket(Products)
                    loyalty_number=id(cust)
                else:
                    cust=Customer(Products)
                    if cust.loyal:
                        loyal_customers.append(cust)
                    loyalty_number=0
                data.append([i+1,loyalty_number,cust.basket])
        self.data=data

    def create_file(self,filename="Sale_History.csv"):
        outfile=open(filename,"wb")
        output=csv.writer(outfile)
        for row in self.data:
            output.writerow(row)
        outfile.close()
        print "---------------------"
        print ""
        print "Output file: %s created with %s baskets over %s days:"%(filename,len(self.data)-1,self.Days)
        print ""
        print "---------------------"

if len(sys.argv)==1:
    if "Stock_Report.csv" not in files_in_directory:
        print "-----"
        print ""
        print "No Stock Report file found."
        print ""
        print "-----"
    else:
        Stock_Report="Stock_Report.csv"
else:
    Stock_Report=argv[1]

Products=import_file(Stock_Report)
a=Sale_History(Products,1000,30)
a.create_file()
