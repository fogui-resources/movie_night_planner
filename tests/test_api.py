from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Movie & TV Show Recommender API!"}

def test_get_popular_movies():
    response = client.get("/movies/popular")
    assert response.status_code == 200
    assert "results" in response.json()

def test_search_movie():
    response = client.get("/movies/search/", params={"query": "Interstellar"})
    assert response.status_code == 200
    assert "results" in response.json()

def test_get_top_rated_tv_shows():
    response = client.get("/tv/top-rated")
    assert response.status_code == 200
    assert "results" in response.json()
