# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 19:05:57 2015

@author: jorgemirandamontano
"""

#Question 1

import pandas as pd
yelp = pd.read_csv('yelp.csv')

#Question 2

fivetoone = yelp[(yelp.stars==5) | (yelp.stars==1)]

#Question 3

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(fivetoone.text, fivetoone.stars, random_state=1)

#Question 4

from sklearn.feature_extraction.text import CountVectorizer

vect = CountVectorizer()
X_train_dtm = vect.fit_transform(X_train)
X_test_dtm = vect.transform(X_test)

# Question 5

from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(X_train_dtm, y_train)
y_pred_class = nb.predict(X_test_dtm)

from sklearn import metrics
print metrics.accuracy_score(y_test, y_pred_class)
#0.918786692759

# Question 6

import numpy as np

y_pred_prob = nb.predict_proba(X_test_dtm)[:, 1]
y_test_binary = np.where(y_test==5, 1, 0)
print metrics.roc_auc_score(y_test_binary, y_pred_prob)
#0.940353585141

# Question 7
import matplotlib.pyplot as plt
fpr, tpr, thresholds = metrics.roc_curve(y_test_binary, y_pred_prob)
plt.plot(fpr, tpr)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('FP')
plt.ylabel('TP')

# Question 8

print metrics.confusion_matrix(y_test, y_pred_class)
'''
[[126  58]
 [ 25 813]]
 '''
813 / float(25 + 813) #0.9701670644391408
126 / float(126 + 58) #0.6847826086956522

# Question 9

X_test[y_test < y_pred_class]
X_test[y_test > y_pred_class]




