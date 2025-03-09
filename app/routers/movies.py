from fastapi import APIRouter
from app.tmdb_service import fetch_popular_movies, fetch_top_rated_movies, search_movie

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.get("/popular")
def get_popular_movies():
    """Fetch popular movies."""
    return fetch_popular_movies()

@router.get("/top-rated")
def get_top_rated_movies():
    """Fetch top-rated movies."""
    return fetch_top_rated_movies()

@router.get("/search/")
def search_movies(query: str):
    """Search for a movie."""
    return search_movie(query)
