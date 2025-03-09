from pydantic import BaseModel
from typing import List, Optional

class Movie(BaseModel):
    id: int
    title: str
    overview: str
    release_date: Optional[str] = None
    vote_average: float
    vote_count: int
    poster_path: Optional[str] = None

class MovieResponse(BaseModel):
    results: List[Movie]

class TVShow(BaseModel):
    id: int
    name: str
    overview: str
    first_air_date: Optional[str] = None
    vote_average: float
    vote_count: int
    poster_path: Optional[str] = None

class TVShowResponse(BaseModel):
    results: List[TVShow]
