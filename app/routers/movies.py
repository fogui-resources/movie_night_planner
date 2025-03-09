from fastapi import APIRouter
from app.tmdb_service import fetch_popular_movies, fetch_top_rated_movies, search_movie
from app.models import MovieResponse

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.get("/popular", response_model=MovieResponse)
def get_popular_movies():
    """Fetch popular movies."""
    return fetch_popular_movies()

@router.get("/top-rated", response_model=MovieResponse)
def get_top_rated_movies():
    """Fetch top-rated movies."""
    return fetch_top_rated_movies()

@router.get("/search/", response_model=MovieResponse)
def search_movies(query: str):
    """Search for a movie."""
    return search_movie(query)
