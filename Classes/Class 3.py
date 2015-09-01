# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 19:12:02 2015

@author: jorgemirandamontano
"""


movies = ['tt0111161', 'tt1856010', 'tt0096694', 'tt0088763', 'tt1375666']
for movie in movies:
    print movie[2:]
    
numbers = [movie[2:] for movie in movies]

#numbers = [] 

#for movie in movies:
 #       print numbers.append(movie[2:0])

#How to add strings with a list comprehension
sum ([int(i) for i in numbers])


open ('airlines.csv') #read mode
open ('airlines.csv', mode='rU') # universal mode
f = open ('airlines.csv', mode='rU') # ready to read
file_string = f.read() #returns one big string in one line
#\n represetns the end of a line
f.close() #file connection now is closed
with open ('airlines.csv', mode='rU') as f:
    file_string = f.read() #context manager

# read the file into a list
with open ('airlines.csv', mode='rU') as f:
    file_list = []
    for row in f:
        file_list.append(row)
#when you iterate thorugh a file you get back rows

len (file_list)
#always check the length of your objects

with open ('airlines.csv', mode='rU') as f:
    file_list = []
    for row in f:
        file_list.append(row)


#Now with list comprehension
with open ('airlines.csv', mode='rU') as f:
    file_list = [row for row in f]

#splitting strings
'Hello DAT students' .split()
'Hello DAT students' .split('e')
'Hello DAT students' .split('\n')

with open ('airlines.csv', mode='rU') as f:
    file_list = [row.split(',') for row in f]



#getting rid off \n
import csv
with open ('airlines.csv', mode='rU') as f:
    file_nested_list = [row for row in csv.reader(f)]
    
file_nested_list[53]

header = file_nested_list[0]
data = file_nested_list[1:]

data[0[3]]

inc1 = []
for inc in data:
    inc1.append(inc[2])
    
inc2 = []
for inc in data:
    inc2.append(inc[5])
    
def sum ():
    return inc1+inc2    
    
average1 = sum()

from __future__ import division
avg = []
for x in average1:
    print int(x) / 30

#SOLUTION
#1
incidents = []
for row in data:
    incidents.append(round((int(row[2]) + int(row[5]))/float(30), 2))


avg_price=[]
for row in data:
    avg_price.append(row[4]/2)
    
#2
airlines=[]
starred=[]
for row in data:
    if row[0][-1] == '*':
        starred.append(1)
        airlines.append(row[0][:-1])
    else: 
        starred.append(0)
    
    
        
dict(zip(airlines, incidents))

my_list ={1,2,1}
set(my_list)
len(set(my_list))

1 in my_list

'name' in my_dict
