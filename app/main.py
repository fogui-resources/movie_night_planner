from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import movies, tv_shows

app = FastAPI(title="Movie & TV Show Recommender API")

# Serve the static frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers for different functionalities
app.include_router(movies.router)
app.include_router(tv_shows.router)

@app.get("/")
def home():
    return {"message": "Welcome to the Movie & TV Show Recommender API!"}
