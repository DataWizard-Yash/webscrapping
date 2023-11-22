import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate as tab


new_on_netflix = 'https://www.imdb.com/list/ls523102783/?ref_=watch_wchgd_1_1_m_wtw_netflix_nov23_i&sort=moviemeter,asc&st_dt=&mode=detail&page=1'

response = requests.get(new_on_netflix)
page_content = BeautifulSoup(response.content, "html.parser")

movie_data = page_content.find('div', 'lister-list')

# Find all individual movie items
movies = movie_data.find_all('div', class_='lister-item-content')

# List to store movie details
movie_details = []

# Extract movie details
for movie in movies:
    # Extracting movie title
    title = movie.find('h3', class_='lister-item-header').a.text.strip()
    
    # Extracting movie year
    year = movie.find('span', class_='lister-item-year').text.strip('()')
    
    # Extracting movie rating
    rating = movie.find('span', class_='ipl-rating-star__rating').text if movie.find('span', class_='ipl-rating-star__rating') else 'Not rated'
    
    # Adding movie details to the list
    movie_details.append({'Title': title, 'Year': year, 'Rating': rating})

# Sort movies by rating in descending order
sorted_movies = sorted(movie_details, key=lambda x: float(x['Rating']) if x['Rating'] != 'Not rated' else 0, reverse=True)

# Create a table and display sorted movie details
table = tab(sorted_movies, headers="keys", tablefmt="pretty")

print(table)


