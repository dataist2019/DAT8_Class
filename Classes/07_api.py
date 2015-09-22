'''
CLASS: Getting Data from APIs

What is an API?
- Application Programming Interface
- Structured way to expose specific functionality and data access to users
- Web APIs usually follow the "REST" standard

How to interact with a REST API:
- Make a "request" to a specific URL (an "endpoint"), and get the data back in a "response"
- Most relevant request method for us is GET (other methods: POST, PUT, DELETE)
- Response is often JSON format
- Web console is sometimes available (allows you to explore an API)
'''

# read IMDb data into a DataFrame: we want a year column!
import pandas as pd
movies=pd.read_csv('imdb_1000.csv')
movies.head()

# use requests library to interact with a URL
import requests
r = requests.get('http://www.omdbapi.com/?t=top+gun&y=&plot=short&r=json')
# check the status: 200 means success, 4xx means error
r.status_code

# view the raw response text
r.text

# decode the JSON response body into a dictionary
r.json()

# extracting the year from the dictionary
r.json()['Year']

# what happens if the movie name is not recognized?

# define a function to return the year
def get_movie_year(title):
    #call url and store the response
    r = requests.get('http://www.omdbapi.com/?t=' +title + '&plot=short&r=json')
    #decode the JSON
    info = r.json()
    #check for success
    if info['Response']=='True':
        return int(info['Year'])
    else:
        return None
    #if success, return Year as integer
    #if not, return None
    


# test the function
get_movie_year('top gun')
# create a smaller DataFrame for testing
top_movies=movies.head().copy()
# write a for loop to build a list of years
years=[get_movie_year(title)  for title in top_movies.title]
from time import sleep
for title in top_movies.title:
    years.append(get_movie_year(title))
    sleep(1)
    #sleep adds 1 second delay
# check that the DataFrame and the list of years are the same length


# save that list as a new column
top_movies['year']=years
'''
Bonus content: Updating the DataFrame as part of a loop
'''

# enumerate allows you to access the item location while iterating
letters = ['a', 'b', 'c']
for index, letter in enumerate(letters):
    print index, letter

# iterrows method for DataFrames is similar
for index, row in top_movies.iterrows():
    print index, row.title

# create a new column and set a default value
movies['year'] = -1

# loc method allows you to access a DataFrame element by 'label'
movies.loc[0, 'year'] = 1994

# write a for loop to update the year for the first three movies
for index, row in movies.iterrows():
    if index < 3:
        movies.loc[index, 'year'] = get_movie_year(row.title)
        sleep(1)
    else:
        break

'''
Other considerations when accessing APIs:
- Most APIs require you to have an access key (which you should store outside your code)
- Most APIs limit the number of API calls you can make (per day, hour, minute, etc.)
- Not all APIs are free
- Not all APIs are well-documented
- Pay attention to the API version

Python wrapper is another option for accessing an API:
- Set of functions that "wrap" the API code for ease of use
- Potentially simplifies your code
- But, wrapper could have bugs or be out-of-date or poorly documented
'''
