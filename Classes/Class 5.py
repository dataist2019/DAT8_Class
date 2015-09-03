# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:40:42 2015

@author: jorgemirandamontano
"""

import pandas as pd

drinks = pd.read_table('drinks.csv', sep='=')
drinks = pd.read_csv('drinks.csv')

drinks.rename(columns={'beer_servings':'beer', 'wine_servings':'wine'})
drinks.rename(columns={'beer_servings':'beer', 'wine_servings':'wine'}, inplace=True)

drinks.index # it's axis O
drinks.columns #It's axis 1

inplace=True #It permanently makes the change

NA # It was converted to NaN

drinks.beer > 5 #Boolean result
drinks[drinks.beer > 5] #returns the result for that condition


drinks.isnull().sum() # Should be the first code I run when opening a dataset

