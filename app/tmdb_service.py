import os
import requests
from dotenv import load_dotenv

# Load API Key
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

BASE_URL = "https://api.themoviedb.org/3"

def fetch_popular_movies():
    """Fetch a list of popular movies."""
    url = f"{BASE_URL}/movie/popular"
    params = {"api_key": TMDB_API_KEY}
    return _make_request(url, params)

def fetch_top_rated_movies():
    url = f"{BASE_URL}/movie/top_rated"
    params = {"api_key": TMDB_API_KEY}
    return _make_request(url, params)

def search_movie(query):
    """Search for a movie by name."""
    url = f"{BASE_URL}/search/movie"
    params = {"api_key": TMDB_API_KEY, "query": query}
    return _make_request(url, params)

def fetch_top_rated_tv_shows():
    """Search for top-rated TV series"""
    url = f"{BASE_URL}/tv/top_rated"
    params = {"api_key": TMDB_API_KEY}
    return _make_request(url, params)

def _make_request(url, params):
    """Helper function to handle API requests."""
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return {"error": f"Failed to fetch data, status: {response.status_code}"}

# Test the functions
if __name__ == "__main__":
    print("Popular Movies:", fetch_popular_movies())
    print("Search Movie (Interstellar):", search_movie("Interstellar"))
    print("Top Rated TV Shows:", fetch_top_rated_tv_shows())
