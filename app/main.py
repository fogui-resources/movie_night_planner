from fastapi import FastAPI
from app.routers import movies, tv_shows

app = FastAPI(title="Movie & TV Show Recommender API")

# Include routers for different functionalities
app.include_router(movies.router)
app.include_router(tv_shows.router)

@app.get("/")
def home():
    return {"message": "Welcome to the Movie & TV Show Recommender API!"}
