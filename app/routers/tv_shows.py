from fastapi import APIRouter
from app.tmdb_service import fetch_top_rated_tv_shows
from app.models import TVShowResponse

router = APIRouter(prefix="/tv", tags=["TV Shows"])

@router.get("/top-rated", response_model=TVShowResponse)
def get_top_rated_tv_shows():
    """Fetch top-rated TV shows."""
    return fetch_top_rated_tv_shows()
