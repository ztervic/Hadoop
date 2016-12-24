#!/usr/bin/env python

import sys

count = 0
maxKey = None
oldKey = None
max=0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, web = data_mapped

    if oldKey and oldKey != thisKey:
        count = 0

    oldKey=thisKey
    count += 1
    if count>max:
        max=count
        maxKey=thisKey


print maxKey, "\t", max

