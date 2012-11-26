#! /usr/bin/env python
import csv
import random
"""
This file generate a data file to be used as the Stock Report for the challenge. The code randomly picks departments and then for each department randomly picks products. The possibilities to choose from are listed in a list: "Departments" and a dictionary: "Products".

There are also two dictionaries for the price and the value in loyalty points of each product.

One can input the name of the file that is produced (Default: "Stock_Report.csv") and also modify the probability of picking a department and a product (Default: .8 and .8). The reason for the randomness is to ensure that it is possible to create a new set of Stock Reports as required.
"""

#Uncomment if you want to stick to a random seed (ie recreate same Stock Report again and again).
#random.seed(1)

#List of departments:
Departments=["Fresh Food","Bakery","Food Cupboard","Frozen Food","Drinks","Baby","Health and Beauty","Pets","Household","Home and Entertainments"]

#Dictionary of products by department:
Products={"Fresh Food":["Apples","Bananas","Fresh Milk","Eggs","Fresh Beef","Fresh Lamb","Fresh Fish","Desserts","Fresh Pasta","Fresh Pizza","Fresh Flowers"],"Bakery":["Bread","Bagel","Pitta","Naan","Croissant","Crumpet","Sweet Treats","Cake"],"Food Cupboard":["Dried Fruit and Nuts","Soup","Tinned Fruit","Gravy","Oil","Cous cous","Rice","Vinegar","Antipasti","Olives","Pickles","Flour","Icing Sugar","Cereal Bars","Popcorn","Jam"],"Frozen Food":["Frozen Meat","Frozen Burgers","Frozen Poultry","Frozen Fruit","Frozen Desserts","Ice Cubes","Frozen Pizza","Frozen Party Food"],"Drinks":["Lemonade","Cola","Sports and Energy","Still Water","Sparkling Water","Fresh Fruit Juice","Tea","Coffee"],"Baby":["Nappies","Baby Toiletries","Baby Rice","Baby Jars"],"Health and Beauty":["Shampoo","Conditioner","Dental Floss","Toothpaste","Toothbrush","Soap","Contact Lens Solution","Cosmetics"],"Pets":["Cat Food","Kitten Food","Dog Food","Puppy Food","Christmas Cat Gift","Christmas Dog Gift"],"Household":["Washing Powder","Bathroom Cleaner","Kitchen Roll","Tissues","Bulbs"],"Home and Entertainments":["Christmas Cards","CD","DVD","Blu Ray","TV","Computer","Utensils","Glasses"]}

Prices={"Apples":1,"Bananas":1.50,"Fresh Milk":2,"Eggs":1,"Fresh Beef":3,"Fresh Lamb":3.5,"Fresh Fish":3,"Desserts":2,"Fresh Pasta":1,"Fresh Pizza":1.5,"Fresh Flowers":4,"Bread":.5,"Bagel":1,"Pitta":1,"Naan":1,"Croissant":1.5,"Crumpet":1.5,"Sweet Treats":3,"Cake":4,"Dried Fruit and Nuts":.5,"Soup":.5,"Tinned Fruit":1,"Gravy":2,"Oil":.5,"Cous cous":1,"Rice":1,"Vinegar":.5,"Antipasti":2,"Olives":1.5,"Pickles":1,"Flour":.5,"Icing Sugar":2,"Cereal Bars":1.5,"Popcorn":2.5,"Jam":2,"Frozen Meat":2.5,"Frozen Burgers":2,"Frozen Poultry":2.5,"Frozen Fruit":1.5,"Frozen Desserts":1.5,"Ice Cubes":1,"Frozen Pizza":1.5,"Frozen Party Food":2,"Lemonade":1.5,"Cola":2,"Sports and Energy":2.5,"Still Water":1,"Sparkling Water":1.5,"Fresh Fruit Juice":2,"Tea":3,"Coffee":2.5,"Nappies":5,"Baby Toiletries":5.5,"Baby Rice":1,"Baby Jars":1.5,"Shampoo":3,"Conditioner":3,"Dental Floss":2.5,"Toothpaste":3,"Toothbrush":3.5,"Soap":1.5,"Contact Lens Solution":5,"Cosmetics":5,"Cat Food":4,"Kitten Food":3.5,"Dog Food":4,"Puppy Food":3.5,"Christmas Cat Gift":9,"Christmas Dog Gift":8.5,"Washing Powder":6,"Bathroom Cleaner":3,"Kitchen Roll":2.5,"Tissues":1.5,"Bulbs":3,"Christmas Cards":4,"CD":8,"DVD":10,"Blu Ray":15,"TV":312,"Computer":600,"Utensils":8,"Glasses":3}

Loyalty_Points={"Apples":10,"Bananas":20,"Fresh Milk":10,"Eggs":10,"Fresh Beef":45,"Fresh Lamb":35,"Fresh Fish":30,"Desserts":15,"Fresh Pasta":10,"Fresh Pizza":25,"Fresh Flowers":20,"Bread":5,"Bagel":10,"Pitta":20,"Naan":10,"Croissant":15,"Crumpet":20,"Sweet Treats":30,"Cake":40,"Dried Fruit and Nuts":7,"Soup":8,"Tinned Fruit":12,"Gravy":22,"Oil":7,"Cous cous":14,"Rice":9,"Vinegar":56,"Antipasti":23,"Olives":17,"Pickles":13,"Flour":56,"Icing Sugar":21,"Cereal Bars":15,"Popcorn":35,"Jam":21,"Frozen Meat":23,"Frozen Burgers":18,"Frozen Poultry":19,"Frozen Fruit":14,"Frozen Desserts":15,"Ice Cubes":12,"Frozen Pizza":17,"Frozen Party Food":32,"Lemonade":19,"Cola":20,"Sports and Energy":27,"Still Water":12,"Sparkling Water":16,"Fresh Fruit Juice":24,"Tea":33,"Coffee":26,"Nappies":53,"Baby Toiletries":55,"Baby Rice":10,"Baby Jars":17,"Shampoo":35,"Conditioner":32,"Dental Floss":12,"Toothpaste":32,"Toothbrush":31,"Soap":11,"Contact Lens Solution":51,"Cosmetics":48,"Cat Food":43,"Kitten Food":36,"Dog Food":72,"Puppy Food":35,"Christmas Cat Gift":99,"Christmas Dog Gift":85,"Washing Powder":66,"Bathroom Cleaner":32,"Kitchen Roll":23,"Tissues":15,"Bulbs":10,"Christmas Cards":52,"CD":160,"DVD":200,"Blu Ray":300,"TV":7000,"Computer":12000,"Utensils":89,"Glasses":53}

class Supermarket():
    """
    This class defines a supermarket by picking a set of departments and products as required. There is a "create_file" method that outputs a csv file.
    """
    def __init__(self,Proportion_Of_Departments=.8,Proportion_Of_Products=.8):
        #Initialise a library
        self.products={}
        for e in Products:
            #Pick (or not) a department:
            if random.random()<Proportion_Of_Departments:
                #Temporary list of products for chosen department:
                temp_list=[]
                #Pick (or not) a product:
                for i in Products[e]:
                    if random.random()<Proportion_Of_Products:
                        temp_list.append(i)
                    #define department value in dictionary:
                    self.products[e]=temp_list

    def create_file(self,filename="Stock_Report.csv"):
        #Output data to csv file.
        data=[["Department","Product","Price","Loyalty_Points"]]
        for e in self.products:
            for i in self.products[e]:
                data.append([e,i,Prices[i],Loyalty_Points[i]])
        outfile=open(filename,"wb")
        output=csv.writer(outfile)
        for row in data:
            output.writerow(row)
        outfile.close()
        print "---------------------"
        print ""
        print "Output file: %s created with the following %s departments and number of products:"%(filename,len(self.products))
        print ""
        for e in self.products:
            print "\t%s: %s products"%(e,len(self.products[e]))
        print ""
        print "---------------------"


a=Supermarket(.8,.8)
a.create_file()
