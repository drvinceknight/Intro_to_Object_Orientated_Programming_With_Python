#Scenario Generator

This directory contains 4 python files:

## Stock_Report_Generator.py

Creates a csv file entitled "Stock_Report.csv" with 4 columns of data: Department, Product, Price and Loyalty_Points.

## Sale_History_Generator.py

Uses "Stock_Report.csv" to generate a history of sales over 31 days (by default). Stochasticity is given to an individual buyer if he/she signs up to the loyalty scheme (a particular customer might be more likely to buy a certain type of product). This outputs a file entitled "Sale_History.csv" with 3 columns of data: Date, Loyalty Number, Basket.

## Promotion_History_Generator.py

Uses "Stock_Report.csv" and "Sale_History.csv" to generate promotions by department for all dates included in the sale history. This outputs a file entitled "Promotions_History.csv" with 3 columns of data: Date, Department and Percent Reduction.

## Generate_Scenario.py

This is a script that simply runs the previous 3 files together (the reason that they are separate is so that they can be run independently if required).
