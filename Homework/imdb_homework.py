# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 10:19:53 2015

@author: jorgemirandamontano
"""


import pandas as pd
import matplotlib.pyplot as plt

#Question 1
# read in 'imdb_1000.csv' and store it in a DataFrame named movies
movies = pd.read_csv('imdb_1000.csv')

#Question 2
# check the number of rows and columns
movies.shape
movies.index
movies.columns

#Question 3
# check the data type of each column
movies.dtypes

#Question 4
# calculate the average movie duration
movies.duration.mean()

#Question 5
# sort the DataFrame by duration to find the shortest and longest movies
movies.sort('duration')
movies.sort('duration', ascending=False)

#Question 6
# create a histogram of duration, choosing an "appropriate" number of bins
movies.duration.plot(kind='hist', bins=18, title='Duration of Top 1000 movies in IMDB')

#Question 7
# use a box plot to display that same data
movies.duration.plot(kind='box', title='Duration of Top 1000 movies in IMDB')

#Question 8
# count how many movies have each of the content ratings
movies.content_rating.value_counts()

#Question 9
# use a visualization to display that same data, including a title and x and y labels
movies.content_rating.value_counts().plot(kind='bar')
plt.xlabel('Rating Type')
plt.ylabel('Frequency')

#Question 10
# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP
movies.content_rating.replace(['NOT RATED', 'APPROVED', 'PASSED', 'GP'], 'UNRATED', inplace=True)


#Question 11
# convert the following content ratings to "NC-17": X, TV-MA
movies.content_rating.replace(['X', 'TV-MA'], 'NC-17', inplace=True)


#Question 12
# count the number of missing values in each column
movies.isnull().sum()


#Question 13
# if there are missing values: examine them, then fill them in with "reasonable" values
movies[movies.content_rating.isnull()]
movies.content_rating.fillna(value='R', inplace=True)


#Question14
# calculate the average star rating for movies 2 hours or longer,
movies[movies.duration>=120].star_rating.mean()


#Question 15
# and compare that with the average star rating for movies shorter than 2 hours
movies[movies.duration<120].star_rating.mean()


#Question 16
# use a visualization to detect whether there is a relationship between duration and star rating
pd.scatter_matrix(movies[['duration', 'star_rating']])

#Question 17
# calculate the average duration for each genre
movies.groupby('genre').duration.mean()

#Question 18
# visualize the relationship between content rating and duration
movies.duration.hist(by=movies.content_rating, sharex=True)

#Question 19
# determine the top rated movie (by star rating) for each genre
movies.sort('star_rating', ascending=False).groupby('genre').max()

# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates
movies.duplicated().sum()

# calculate the average star rating for each genre, but only include genres with at least 10 movies
top_genres=['Drama', 'Comedy', 'Action', 'Crime', 'Biography', 'Adventure', 'Animation', 'Horror', 'Mystery']
movies[movies.genre.isin(top_genres)].groupby('genre').star_rating.mean()

