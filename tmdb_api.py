import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")

print(API_KEY)

# searching for the movie
def movie_search(movie_name):
    url = "https://api.themoviedb.org/3/search/movie"

    # the parameteres of the search
    params = {
        "api_key": API_KEY,
        "query": movie_name
    }

    # error codes
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

    print("Something went wrong", response.status_code)
    return None
