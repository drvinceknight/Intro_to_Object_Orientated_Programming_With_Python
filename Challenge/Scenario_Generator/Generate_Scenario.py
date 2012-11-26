#! /usr/bin/env python
import os

"""
This file generates all three reports needed to run the supermarket challenge. Note that this is done by running three separate scripts. This is so that each file can also be run independently.
"""

print "---------------------------------"
print ""
print "Generating Stock Report using 'Stock_Report_Generator.py' (modify file to change parameters as required)"
os.system("./Stock_Report_Generator.py")
print ""
print "---------------------------------"
print "---------------------------------"
print ""
print "Generating Sale History using 'Sale_History_Generator.py' (modify file to change parameters as required)"
os.system("./Sale_History_Generator.py")
print ""
print "---------------------------------"
print "---------------------------------"
print ""
print "Generating Promotions History using 'Promotion_History.py' (modify file to change parameters as required)"
os.system("./Promotion_History_Generator.py")
print ""
print "---------------------------------"
