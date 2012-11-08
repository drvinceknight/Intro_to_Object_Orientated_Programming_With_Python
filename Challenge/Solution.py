#! /usr/bin/env python
from __future__ import division
import csv

"""
This file contains code for the solution of the Supermarket challenge.
"""

class Product():
    """
    A class for every product
    """
    def __init__(self,Prod_Name,Price,Loyalty_Points,Department):
        self.name=Prod_Name
        self.price=Price
        self.loyalty_points=Loyalty_Points
        self.department=Department

    def cost(self,Date):
        cost=self.price
        if Date in self.department.prom_history:
            cost*=(1-self.department.prom_history[Date]/100)
        return cost

class Department():
    """
    A class for each department.
    """
    def __init__(self,Dep_Name,Stock_Report,Promotions_History):
        self.name=Dep_Name

        self.products=[]
        for e in Stock_Report:
            if self.name==e[0]:
                self.products.append(Product(e[1],e[2],e[3],self))

        prom_history={}
        for e in Promotions_History:
            if self.name==e[1]:
                prom_history[e[0]]=e[2]
        self.prom_history=prom_history

class Basket():
    """
    A class for each basket used by each customer, note that it is date dependant.
    """
    def __init__(self,Product_List,Date,String_to_Product_Dictionary):
        self.products=[String_to_Product_Dictionary[e] for e in Product_List]
        self.data=Date
        self.cost=0
        self.loyalty_points=0
        for e in self.products:
            self.cost+=e.cost(Date)
            self.loyalty_points+=e.loyalty_points


def Import_Stock_Report(Stock_Report="Stock_Report.csv"):
    """
    Import the Stock report
    """
    outfile=open(Stock_Report,"rb")
    raw_data=csv.reader(outfile)
    data=[row for row in raw_data]
    outfile.close()
    data=[[e[0],e[1],eval(e[2]),eval(e[3])] for e in data[1:]]
    return data

def Import_Promotions_History(Promotions_History="Promotions_History.csv"):
    """
    Import the Promotions History
    """
    outfile=open(Promotions_History,"rb")
    raw_data=csv.reader(outfile)
    data=[row for row in raw_data]
    outfile.close()
    data=[[eval(e[0]),e[1],eval(e[2])] for e in data[1:]]
    return data

def Import_Sales_History(Sale_History="Sale_History.csv"):
    """
    Import the Sales History
    """
    outfile=open(Sale_History,"rb")
    raw_data=csv.reader(outfile)
    data=[row for row in raw_data]
    outfile.close()
    data=[[eval(e[0]),eval(e[1]),eval(e[2])] for e in data[1:]]
    return data

def Create_Departments(Promotions_History,Stock_Report):
    """
    Create all departments and products
    """
    Department_Names=list(set([e[0] for e in Stock_Report]))
    Departments=[]
    for e in Department_Names:
        Departments.append(Department(e,Stock_Report,Promotions_History))
    return Departments

def Create_String_to_Product_Dictionary(Departments):
    d={}
    for e in Departments:
        for i in e.products:
            d[i.name]=i
    return d


class Challenge_Solution():
    """
    This class solves the challenge
    """
    def __init__(self,Stock_Report="Stock_Report.csv",Promotions_History="Promotions_History.csv",Sale_History="Sale_History.csv"):
        #Import data
        self.promotions_history=Import_Promotions_History(Promotions_History)
        self.stock_report=Import_Stock_Report(Stock_Report)
        self.sale_history=Import_Sales_History(Sale_History)
        self.number_of_sales=len(self.sale_history)
        #Create departments
        self.departments=Create_Departments(self.promotions_history,self.stock_report)
        #Create string to products dictionary
        self.string_to_product_dictionary=Create_String_to_Product_Dictionary(self.departments)
        #Initialise loyal customers dictionary
        self.loyal_customers={}
        #Initialise sales figure
        self.sales=0
        for e in self.sale_history:
            basket=Basket(e[2],e[0],self.string_to_product_dictionary)
            self.sales+=basket.cost
            if e[1] in self.loyal_customers:
                self.loyal_customers[e[1]]+=basket.loyalty_points
            else:
                self.loyal_customers[e[1]]=basket.loyalty_points

    def output_loyalty_report(self,loyalty_report="Loyalty_Report.csv"):
        outfile=open(loyalty_report,"wb")
        output=csv.writer(outfile)
        output.writerow(["Loyalty Number (0=Not in Scheme)","Loyalty Points"])
        for e in self.loyal_customers:
            output.writerow([e,self.loyal_customers[e]])
        outfile.close()
        print "--------------------"
        print ""
        print "Output file: %s created with %s loyalty customer details over a total of %s sales."%(loyalty_report,len(self.loyal_customers),self.number_of_sales)
        print ""
        print "--------------------"


a=Challenge_Solution()
print "--------------------"
print ""
print "Total sales: %s over a total of %s sales."%(a.sales,a.number_of_sales)
print ""
print "--------------------"
a.output_loyalty_report()
