#! /usr/bin/env python
import csv
import random
import os
import sys

#random.seed(1)


files_in_directory=os.listdir(".")

if len(sys.argv)==1:
    if "Stock_Report.csv" not in files_in_directory:
        print "-----"
        print ""
        print "No Stock Report file found."
        print ""
        print "-----"
    else:
        Stock_Report="Stock_Report.csv"
    if "Sale_History.csv" not in files_in_directory:
        print "-----"
        print ""
        print "No Sale History file found."
        print ""
        print "-----"
    else:
        Sale_History="Sale_History.csv"
else:
    Stock_Report=argv[1]
    Sale_History=argv[2]

outfile=open(Sale_History,"rb")
dates=csv.reader(outfile)
dates=[row for row in dates]
dates=list(set([eval(e[0]) for e in dates[1:]]))
outfile.close()

outfile=open(Stock_Report,"rb")
departments=csv.reader(outfile)
departments=[row for row in departments]
departments=list(set([e[0] for e in departments[1:]]))
outfile.close()

Promotions=[i*10 for i in range(1,10)]

promotion_dict={}
for e in departments:
    promotion_dict[e]=random.random()

filename="Promotions_History.csv"

file=open(filename,"wb")
output=csv.writer(file)
output.writerow(["Date","Department","Percent Reduction"])
k=0
for i in dates:
    for e in departments:
        if random.random()<promotion_dict[e]:
            k+=1
            output.writerow([i,e,random.choice(Promotions)])
file.close()

print "-----------------------------"
print ""
print "Output file: %s created with %s sales over %s days."%(filename,k,len(dates))
print ""
print "-----------------------------"
