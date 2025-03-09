# Movie & TV Show Recommender API

![License](https://img.shields.io/github/license/freedomofchoice1991/movie_night_planner)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![HTML](https://img.shields.io/badge/HTML-5-orange)
![GitHub issues](https://img.shields.io/github/issues/freedomofchoice1991/movie_night_planner)
![Last Commit](https://img.shields.io/github/last-commit/freedomofchoice1991/movie_night_planner)
![Repo Size](https://img.shields.io/github/repo-size/freedomofchoice1991/movie_night_planner)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)
![Contributions](https://img.shields.io/badge/contributions-welcome-yellow.svg)
![TMDb API](https://img.shields.io/badge/TMDb-API-blue)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/freedomofchoice1991/movie_night_planner)



## Overview
This is a **FastAPI-based application** that suggests movies and TV shows using **The Movie Database (TMDb) API**. Users can:
- Search for movies 🎬
- Get popular & top-rated movies ⭐
- Get recommendations based on input
- Browse top-rated TV shows 📺
- Use a simple frontend to explore movies

## Features
✅ **FastAPI** backend

✅ **TMDb API integration** for movie data

✅ **HTML & JavaScript frontend**

✅ **Dynamic search** with movie posters & descriptions

✅ **Deployment-ready** for local or cloud hosting

---

## 1️⃣ Setup & Installation

### **1.1 Clone the Repository**
Open a terminal and run:
```bash
#  Clone the repository
git clone https://github.com/YOUR_USERNAME/fastapi-movie-recommender.git

# Navigate to the project directory
cd fastapi-movie-recommender
```

### **1.2 Create a Virtual Environment**
Use Python's `venv` to isolate dependencies:
```bash
#  Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### **1.3 Install Dependencies**
```bash
   pip install -r requirements.txt
```

---

## 2️⃣ Get a TMDb API Key
To fetch movies & TV shows, you **must register** for an API key at TMDb:
1. Visit [TMDb API](https://www.themoviedb.org/documentation/api)
2. Sign up & create a developer account
3. Get your **API Key (v3 auth)**
4. Store it in a `.env` file

```bash
#  Create the .env file in your project directory
nano .env
```

Inside `.env`, add:
```ini
TMDB_API_KEY=your_api_key_here
```

---

## 3️⃣ Running the Project Locally

### **3.1 Start the FastAPI Server**
```bash
   uvicorn app.main:app --reload
```
This will run the server at: **http://127.0.0.1:8000/**

### **3.2 Access the Frontend**
Open a browser and go to:
- **Frontend:** [http://127.0.0.1:8000/static/index.html](http://127.0.0.1:8000/static/index.html)
- **API Docs (Swagger UI):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc UI:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 4️⃣ API Endpoints
| Endpoint                           | Method | Description            |
|------------------------------------|--------|------------------------|
| `/movies/popular`                  | `GET`  | Get popular movies     |
| `/movies/top-rated`                | `GET`  | Get top-rated movies   |
| `/movies/search/?query=movie_name` | `GET`  | Search for a movie     |
| `/tv/top-rated`                    | `GET`  | Get top-rated TV shows |

---

## 5️⃣ Deployment Options
### **Option 1: Local (Uvicorn)**
```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### **Option 2: Deploy on Render Website**
#### What is [Render](https://render.com/docs/web-services/)?  A Cloud Application Service provider

#### Think of "Render" as a service that takes your website or application code and makes it live on the internet.


1. **Push your code to GitHub**
```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
```
2. **Go to [Render](https://render.com/)** & create a new **Web Service**
3. **Connect your GitHub repo** & set up environment variables:
   - `TMDB_API_KEY=your_api_key_here`
4. **Deploy** & test it at your Render URL 🚀

---

## 6️⃣ Additional Tips & Tricks
✅ **Use Postman or httpie** to test API requests:
```bash
    http GET http://127.0.0.1:8000/movies/popular
```
✅ **Enable caching** (if needed) using Redis:
```bash
    pip install fastapi-cache2 redis
```
✅ **Customize the frontend** (`static/index.html`, `static/style.css`)
✅ **Secure the API** with authentication if required

---

## 💡 Contribution & Support
- Found a bug? **Open an issue** on GitHub!
- Want to contribute? **Fork & submit a PR** ✨

📌 **Made with ❤️ using FastAPI & TMDb API**

