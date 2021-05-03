#!/usr/bin/env python

from deepdiff import DeepDiff
from deepdiff import grep, DeepSearch
from pprint import pprint
import json
import re
import argparse

def args():
    ''' Argparse takes various arguments that will be specific to the users input. Argparse requires
        the reference json file as well as your test output file. '''
    parser=argparse.ArgumentParser(description = "json stat file comparison for test validation")
    parser.add_argument("-i","--input", help="reference stat file", required = True, type = str)
    parser.add_argument("-f","--user_file", help="stat json for comparison - found in output directory", required = True, type = str)
    return parser.parse_args()
args = args()

#set argparse
input_file = args.input
compare_stat = args.user_file

#load in reference
with open(input_file, "r") as f:
    ref = json.load(f)
f.close()

#load in user test file
with open(compare_stat, "r") as c:
    compare = json.load(c)
c.close()

#threshold for acceptable values 
threshold = 0.001

#Conditional for direct matches
if DeepDiff(ref,compare) == {}:
    print("No differences detected: test validated")
#Conditional for acceptable values
elif DeepDiff(ref,compare) != {}:
    ds = DeepDiff(ref,compare)
    ds = (ds['values_changed'])
    ds = str(ds)
    diff_vals = re.findall(r':\W(\d+)', ds)
    old_val = int(diff_vals[1])
    new_val = int(diff_vals[0])
    if old_val <= (new_val + (new_val*threshold)) and old_val >= (new_val - (new_val*threshold)):
        print("No differences detected: test validated")
    #if not met, test failed
    else:
        print("Test Failed")