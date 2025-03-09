from fastapi import APIRouter
from app.tmdb_service import fetch_top_rated_tv_shows

router = APIRouter(prefix="/tv", tags=["TV Shows"])

@router.get("/top-rated")
def get_top_rated_tv_shows():
    """Fetch top-rated TV shows."""
    return fetch_top_rated_tv_shows()
