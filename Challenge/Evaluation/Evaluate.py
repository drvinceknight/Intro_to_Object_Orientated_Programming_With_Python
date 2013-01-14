#! /usr/bin/env python
from sys import argv, exit
import os
import time

solution_script = "Solution_Script.py"
number_of_runs = 10

original_files = os.listdir("./")
original_files = [e for e in original_files if e[-3:] == "csv"]

if len(original_files) > 4:
    string = "Caution,  more than 4 csv files found in directory"
    print ""
    print (len(string) + 4) * "-"
    print (len(string) + 4) * "-"
    print "!!" + string + "!!"
    print ""
    print "Continue (y, n)?"
    print (len(string) + 4) * "-"
    print (len(string) + 4) * "-"
    print ""
    if raw_input() == "n":
        exit()
    extra_files = [e for e in original_files if e not in ["Loyalty_Report_Solution.csv", "Promotions_History.csv", "Sale_History.csv", "Stock_Report.csv"]]
    for e in extra_files:
        if raw_input("Delete %s (y, n)?" % e) == "y":
            os.system("rm %s" % e)

original_files = os.listdir("./")
original_files = [e for e in original_files if e[-3:] == "csv"]


class Solution_Run():
    def __init__(self, solution_script):
        self.solution_script = solution_script
        self.start_time = time.time()
        try:
            os.system("python %s>>%s_output.txt" % (solution_script, solution_script[:-3]))
            self.run_time = time.time() - self.start_time
        except:
            string = "%s failed" % solution_script
            print len(string) * "-"
            print string
            print len(string) * "-"


if len(argv) == 1:
    """
    Print out input parameters if no options are passed to prompt.
    """
    print """
#Usage

    ./Evaluate [solution_script = "Solution_Script.py"] [number_of_runs = 10]
          """
if len(argv) > 1:
    """
    Read in all input parameters
    """
    solution_script = argv[1]
    try:
        number_of_runs = argv[2]
    except:
        pass

    string = "Running %s runs of %s" % (number_of_runs, solution_script)
    print ""
    print (len(string) + 2) * "-"
    print "|" + string + "|"
    print (len(string) + 2) * "-"
    print ""

    runs = []
    k = 0
    for e in range(number_of_runs):
        runs.append(Solution_Run(solution_script))
        print ""
        print "\tRun number %s took: %s seconds" % (k + 1, runs[-1].run_time)
        if k >= 1:
            if runs[-1].run_time < runs[-2].run_time:
                print "\tDoing better! :)"
            else:
                print "\tDoing worse... :("
        print ""
        k += 1
    average_run_time = sum(a.run_time for a in runs) / number_of_runs
    max_run_time = max(a.run_time for a in runs)
    min_run_time = min(a.run_time for a in runs)

    string = "Average run time over %s runs of %s: %s seconds." % (number_of_runs, solution_script, average_run_time)
    string2 = "Max run time over %s runs of %s: %s seconds." % (number_of_runs, solution_script, max_run_time)
    string3 = "Min run time over %s runs of %s: %s seconds." % (number_of_runs, solution_script, min_run_time)
    print ""
    print (len(string) + 2) * "-"
    print "|" + string2 + (len(string) - len(string2)) * " " + "|"
    print "|" + string + "|"
    print "|" + string3 + (len(string) - len(string3)) * " " + "|"
    print (len(string) + 2) * "-"
    print ""

original_files
new_files = os.listdir("./")
new_files = [e for e in new_files if e not in original_files and e[-3:] == "csv"]


if len(new_files) > 1:
    os.exit("Too many csv files output.")

string = "Comparing '%s' to 'Loyalty_Report_Solution.csv'" % new_files[0]
print ""
print (len(string) + 2) * "-"
print "|" + string + "|"

os.system("diff %s Loyalty_Report_Solution.csv > diff_output.txt" % new_files[0])
size_of_diff_file = 0
with open('diff_output.txt') as diff_output:
    for row in diff_output:
        if row.strip():
            size_of_diff_file += 1

string2 = "Size of diff file is: %s rows." % size_of_diff_file
print "|" + len(string) * " " + "|"
print "|" + string2 + (len(string) - len(string2)) * " " + "|"
print (len(string) + 2) * "-"
print ""
