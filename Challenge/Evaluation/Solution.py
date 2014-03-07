#! /usr/bin/env python
from __future__ import division
import csv

"""
This file contains code for the solution of the Supermarket challenge.

It by default reads data from three files:

- "Stock_Report.csv"
- "Sale_History.csv"
- "Promotions_History.csv"

It prints to screen the total takings and creates a file "Loyalty_Report.csv" which includes details as to the loyalty points collected by each loyal customer.

"""


def import_stock_report(Stock_Report="Stock_Report.csv"):
    """
    Import the Stock report
    """
    outfile = open(Stock_Report, "rb")
    raw_data = csv.reader(outfile)
    data = [row for row in raw_data]
    outfile.close()
    data = [[e[0], e[1], eval(e[2]), eval(e[3])] for e in data[1:]]
    return data


def import_promotions_history(Promotions_History="Promotions_History.csv"):
    """
    Import the Promotions History
    """
    outfile = open(Promotions_History, "rb")
    raw_data = csv.reader(outfile)
    data = [row for row in raw_data]
    outfile.close()
    data = [[eval(e[0]), e[1], eval(e[2])] for e in data[1:]]
    return data


def import_sales_history(Sale_History="Sale_History.csv"):
    """
    Import the Sales History
    """
    outfile = open(Sale_History, "rb")
    raw_data = csv.reader(outfile)
    data = [row for row in raw_data]
    outfile.close()
    data = [[eval(e[0]), eval(e[1]), eval(e[2])] for e in data[1:]]
    return data


def create_departments(Promotions_History, Stock_Report):
    """
    Create all departments and products
    """
    department_Names = list(set([e[0] for e in Stock_Report]))
    departments = []
    for e in department_Names:
        departments.append(Department(e, Stock_Report, Promotions_History))
    return departments


def create_string_to_product_dictionary(departments):
    """
    This creates a dictionary that takes as key a string and returns the product object.
    """
    d = {}
    for e in departments:
        for i in e.products:
            d[i.name] = i
    return d


class Product():
    """
    A class for every product
    """
    def __init__(self, prod_name, price, loyalty_points, department):
        self.name = prod_name
        self.price = price
        self.loyalty_points = loyalty_points
        self.department = department

    def cost(self, Date):
        cost = self.price
        if Date in self.department.prom_history:
            cost *= (1 - self.department.prom_history[Date] / 100)
        return cost


class Department():
    """
    A class for each department.
    """
    def __init__(self, Dep_Name, Stock_Report, Promotions_History):
        self.name = Dep_Name

        self.products = []
        for e in Stock_Report:
            if self.name == e[0]:
                self.products.append(Product(e[1], e[2], e[3], self))

        prom_history = {}
        for e in Promotions_History:
            if self.name == e[1]:
                prom_history[e[0]] = e[2]
        self.prom_history = prom_history


class Basket():
    """
    A class for each basket used by each customer,  note that it is date dependant.
    """
    def __init__(self, Product_List, Date, String_to_Product_Dictionary):
        self.products = [String_to_Product_Dictionary[e] for e in Product_List]
        self.data = Date
        self.cost = 0
        self.loyalty_points = 0
        for e in self.products:
            self.cost += e.cost(Date)
            self.loyalty_points += e.loyalty_points


class Challenge_Solution():
    """
    This class solves the challenge
    """
    def __init__(self, stock_report="Stock_Report.csv", promotions_history="Promotions_History.csv", sale_history="Sale_History.csv"):
        #Import data
        self.promotions_history = import_promotions_history(promotions_history)
        self.stock_report = import_stock_report(stock_report)
        self.sale_history = import_sales_history(sale_history)
        #Create departments
        self.departments = create_departments(self.promotions_history, self.stock_report)
        #Create string to products dictionary
        self.string_to_product_dictionary = create_string_to_product_dictionary(self.departments)
        #Initialise loyal customers dictionary
        self.loyal_customers = {}
        #Initialise sales figure
        self.sales = 0
        for e in self.sale_history:
            basket = Basket(e[2], e[0], self.string_to_product_dictionary)
            self.sales += basket.cost
            if e[1] in self.loyal_customers:
                self.loyal_customers[e[1]] += basket.loyalty_points
            else:
                self.loyal_customers[e[1]] = basket.loyalty_points

    def output_loyalty_report(self, loyalty_report="Loyalty_Report.csv"):
        outfile = open(loyalty_report, "wb")
        output = csv.writer(outfile)
        output.writerow(["Loyalty Number (0 = Not in Scheme)", "Loyalty Points"])
        for e in self.loyal_customers:
            output.writerow([e, self.loyal_customers[e]])
        outfile.close()


a = Challenge_Solution()
print "Total sales: %s." % a.sales
a.output_loyalty_report()
