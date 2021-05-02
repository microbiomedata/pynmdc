#!/usr/bin/env python

from deepdiff import DeepDiff
from deepdiff import grep, DeepSearch
from pprint import pprint
import argparse
import json
import re
#Argparse takes in arguments that are callable when running the code.

def args():
    ''' Argparse takes various arguments that will be specific to the users input. Argparse requires
        the reference json file as well as your test output file. '''
    parser=argparse.ArgumentParser(description = "json stat file comparison for test validation")
    parser.add_argument("-i","--input", help="reference stat file", required = True, type = str)
    parser.add_argument("-s","--compare_stat", help="stat json for comparison - found in output directory", required = True, type = str)
    return parser.parse_args()
args = args()


input_file = args.input
compare_stat = args.compare_stat

with open(input_file, "r") as f:
    ref = json.load(f)
f.close()

with open(compare_stat, "r") as c:
    compare = json.load(c)
c.close()

threshold = 0.001

print(ref)
print(compare)


if DeepDiff(ref,compare) == {}:
    print("No differences detected: test validated")
elif DeepDiff(ref,compare) != {}:
    ds = DeepDiff(ref,compare)
    ds = (ds['values_changed'])
    ds = str(ds)
    diff_vals = re.findall(r':\W(\d+)', ds)
    old_val = int(diff_vals[1])
    new_val = int(diff_vals[0])
    if old_val <= (new_val + (new_val*threshold)) and old_val >= (new_val - (new_val*threshold)):
        print("No differences detected: test validated")
    else:
        print("Test Failed")