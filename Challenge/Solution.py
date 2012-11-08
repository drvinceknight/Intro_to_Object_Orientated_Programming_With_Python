#! usr/bin/env python

"""
This file contains code for the solution of the Supermarket challenge.
"""

class Product()
    """
    A class for every product
    """
    def __init__(self,Prod_Name,Price,Loyalty_Points,Department):
        self.name=Prod_Name
        self.price=Price
        self.loyalty_points=Loyalty_Points
        self.department=Department

    def cost(self,Date):
        self.cost=self.price
        if Date in self.department.prom_history:
            self.cost*=(1-self.department.prom_history[Date]/10)
        return self.cost

class Department():
    """
    A class for each department.
    """
    def __init__(self,Dep_Name,Stock_Report,Promotion_History):
        self.name=Dep_Name

        self.products=[]
        for e in Stock_Report:
            if self.name==e[0]:
                self.products=Product(e[1],e[2],e[3],self)

        prom_history={}
        for e in Promotion_History:
            if self.name==e[1]:
                prom_history[e[0]]=e[2]
        self.prom_history=prom_history

class Basket():
    """
    A class for each basket used by each customer, note that it is date dependant.
    """
    def __init__(self,Product_List,Date):
        self.products=Product_List
        self.data=Date
        self.cost=0
        for e in self.products:
            self.cost+=e.cost(Date)

