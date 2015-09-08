# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 19:37:14 2015

@author: jorgemirandamontano
"""



iris_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class_name']
iris = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=-1)
iris.columns=iris_cols

iris.isnull().sum()

iris.head()
iris.describe()
iris.sepal_length.describe()

iris.sepal_length.value_counts().plot(kind='hist')
iris.sepal_length.plot(kind='hist')
iris.sepal_width.plot(kind='hist')
iris.petal_length.plot(kind='hist')
iris.petal_width.plot(kind='hist')

iris.class_name.value_counts()

iris.groupby('class_name').petal_length.mean().plot(kind='bar')

iris.groupby('class_name').petal_width.mean().plot(kind='bar')

iris.class_name.sort_index()
