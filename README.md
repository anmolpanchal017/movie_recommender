<p align="center">
  <img src="banner.png" width="100%" alt="Movie Recommendation System Banner"/>
</p>

<h1 align="center">🎬 Movie Recommendation System</h1>
<p align="center">
  <b>A Machine Learning + NLP + Flask Powered Intelligent Movie Recommender</b>
  <br>
  <br>
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python"/>
  <img src="https://img.shields.io/badge/Framework-Flask-green?logo=flask"/>
  <img src="https://img.shields.io/badge/ML-NLP-orange?logo=scikitlearn"/>
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen"/>
</p>

---

# 📌 **Project Overview**
This is a **Content-Based Movie Recommendation System** that recommends movies based on **title similarity, keyword matching, and genre filtering**.

It uses:

- **TF-IDF Vectorization**  
- **Cosine Similarity**  
- **NLP-Based Text Processing**  
- **Flask Web Framework**  
- **Beautiful Frontend UI**

The system intelligently analyzes movie descriptions, genres, cast and directors to produce highly accurate recommendations.

---

# 🚀 **Features**

### 🎞️ Movie Recommendation Modes
- 🔍 **Search by Movie Title**
- 🎯 **Search by Keywords**
- 🎭 **Search by Genre**

### 🧠 Intelligent AI / NLP Features
- TF-IDF word vectorization  
- Cosine similarity search  
- Content-based filtering  

### 🌐 Modern UI
- Clean search interface  
- Beautiful movie result cards  
- Responsive layout  
- Loader & animations  

---

# 🛠️ **Tech Stack**

### **Backend**
- Python  
- Flask  
- scikit-learn  
- pandas  
- numpy  
- requests  

### **Frontend**
- HTML  
- CSS  
- Bootstrap  
- JavaScript  

### **Machine Learning**
- TF-IDF Vectorizer  
- Cosine Similarity  

---

# 📂 **Project Structure**

movie_recommender/
│
├── app.py
├── requirements.txt
│
├── src/
│ ├── data_loader.py
│ ├── preprocessing.py
│ ├── recommender.py
│ └── poster_fetcher.py (optional)
│
├── templates/
│ └── index.html
│
├── static/
│ ├── style.css
│ ├── placeholder.png
│ └── posters/ (optional local posters)
│
└── data/
└── imdb_top_1000.csv


---

# 📥 **Installation & Setup**

### **1️⃣ Clone Repository**
```sh
git clone https://github.com/your_username/movie-recommender.git
cd movie-recommender


2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python app.py

🧠 How Recommendation Works (AI Logic)
✔ Step 1 — Data Preprocessing
Merge genre, overview, actors, director
Clean text
Remove missing/duplicate entries
✔ Step 2 — TF-IDF Vectorization
Converts movie text → high-dimensional vector
Based on word importance
✔ Step 3 — Cosine Similarity
Finds movies closest in meaning
Higher value = more similar
✔ Step 4 — Final Recommendation
Extract top 10 most similar movies
Display on UI

📊 Flowchart

Start
   ↓
Load Dataset
   ↓
Preprocessing
   ↓
TF-IDF Vectorization
   ↓
Cosine Similarity
   ↓
User Input (Title | Keyword | Genre)
   ↓
Generate Recommendations
   ↓
Display Output
   ↓
End


🏗️ Architecture Diagram
User → Web UI → Flask Server → ML Model 
     ← Results ← Similarity Engine ← TF-IDF Vectors

🧬 ER Diagram (Conceptual)

 MOVIE
+--------------+
| Movie_ID     |
| Title        |
| Genre        |
| Director     |
| Plot         |
+--------------+
      |
      | 1 - many
      v
 CAST
+--------------+
| Cast_ID      |
| Actor_Name   |
| Movie_ID(FK) |
+--------------+

📚 Dataset Details

Dataset used:
➡ IMDB Top 1000 Movies (Kaggle)

Contains:

Column	Description
Title	          Movie name
Genre	          Movie genres
Director	      Movie director
Star1–Star4	    Actor names
Overview	      Movie plot
IMDB Rating	    Rating out of 10

🧪 Test Cases
Test Case	Input	Output
Title Search	    The Dark Knight	    Similar movies
Genre Search	    Action	            Action movies
Keyword Search	  space adventure	    Interstellar, Gravity, Martian

📝 Conclusion

This project demonstrates the power of Machine Learning + NLP in building a real-world recommendation engine.
It’s fast, accurate, user-friendly, and showcases skills in ML, Flask, data processing, and frontend development.

