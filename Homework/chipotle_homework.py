# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 16:39:35 2015

@author: jorgemirandamontano
"""

##Part 1
import csv

with open('chipotle.tsv', mode='rU') as f:
    file_nested_list = [row for row in csv.reader(f, delimiter='\t')]
    
##Part 2
header = file_nested_list[0]
data = file_nested_list[1:]

##Part 3
orders=len(set([row[0] for row in data]))
prices=[float(row[4][1:-1]) for row in data]

sum(prices) /orders

##Part 4
cans = []
other = []
for row in data:
    if row[2][0:6] == "Canned":
        cans.append(row[3])
        other.append(row[3])

uniq_sodas=[set(cans)]

##Part 5



burrito=0
toppings=0

for row in data:
    if row[2][-7:-1] == 'Burrit':
        burrito +=1
        toppings += (row[3].count(',') + 1)


toppings/float(burrito)
