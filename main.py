from multiprocessing import context
from urllib import response
from fastapi import FastAPI, Request, Form, HTTPException , Cookie
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import List, Optional
from pydantic import BaseModel
import sqlite3
import uvicorn


app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Connexion à la base de données SQLite
conn = sqlite3.connect('votre_base_de_données.db')
cursor = conn.cursor()

# Création de la table des utilisateurs
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT NOT NULL
                  )''')
cursor.execute('''CREATE TABLE IF NOT EXISTS articles (
                    article_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    content TEXT
                  )''')
conn.commit()


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login", response_class=HTMLResponse)
async def login(username: str = Form(...), password: str = Form(...)):
    cursor.execute("SELECT user_id FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    if user:
        return RedirectResponse(url="/success", status_code=303)
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
# #! PAGE DE L'ESPACE UTILISATEUR

@app.get("/user", response_class=HTMLResponse)
async def user_space(request: Request, username: str = Cookie(None)):
    if not username:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    cursor.execute("SELECT article_id, title, content FROM articles WHERE username = ?", (username,))
    articles = cursor.fetchall()
    articles_list = [{"article_id": article[0], "title": article[1], "content": article[2]} for article in articles]
    
    return templates.TemplateResponse("success.html", {"request": request, "username": username, "articles": articles_list})
   
# #!PARTIE CRUD UTILISATEUR

class Article(BaseModel):
    title: str
    content: str
    category: str
    user_id: int

# Opération Create (Créer) : Créer un nouvel article
@app.post("/user/article", response_model=HTMLResponse)
def create_article_user(article: Article):
    cursor.execute('''INSERT INTO articles (title, content, category, user_id)
                      VALUES (?, ?, ?, ?)''', (article.title, article.content, article.category, article.user_id))
    conn.commit()
    return RedirectResponse(url="/user", status_code=303)

# Opération Read (Lire) : Récupérer tous les articles d'un utilisateur
@app.get("/user/{user_id}/articles", response_class=HTMLResponse)
def read_user_articles(user_id: int):
    cursor.execute('''SELECT * FROM articles WHERE user_id = ?''', (user_id,))
    user_articles = cursor.fetchall()
    if not user_articles:
        raise HTTPException(status_code=404, detail="Aucun article trouvé pour cet utilisateur")
    
    articles_html = "<h2>Articles de l'utilisateur</h2>"
    for article in user_articles:
        articles_html += f"<p>Titre: {article[1]}, Contenu: {article[2]}, Catégorie: {article[3]}</p>"

    return HTMLResponse(content=f"<html><body>{articles_html}</body></html>")

# Opération Update (Mettre à jour) : Mettre à jour un article existant
@app.put("/user/article/{article_id}", response_model=HTMLResponse)
def update_article_user(article_id: int, article: Article):
    cursor.execute('''SELECT * FROM articles WHERE id = ?''', (article_id,))
    existing_article = cursor.fetchone()
    if not existing_article:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    
    cursor.execute('''UPDATE articles SET title=?, content=?, category=? WHERE id=?''', 
                   (article.title, article.content, article.category, article_id))
    conn.commit()
    
    return RedirectResponse(url=f"/user/{existing_article[4]}/articles", status_code=303)
# Opération Delete (Supprimer) : Supprimer un article existant
@app.delete("/user/article/{article_id}", response_model=HTMLResponse)
def delete_article_user(article_id: int):
    cursor.execute('''SELECT * FROM articles WHERE id = ?''', (article_id,))
    existing_article = cursor.fetchone()
    if not existing_article:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    
    cursor.execute('''DELETE FROM articles WHERE id = ?''', (article_id,))
    conn.commit()
    
    return RedirectResponse(url=f"/user/{existing_article[4]}/articles", status_code=303)
    
#! --------------------------------------------------------------------------------------------------------------------------------------------------------------------
@app.get("/signup", response_class=HTMLResponse)
async def signup_form(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


@app.post("/signup", response_class=HTMLResponse)
async def signup(username: str = Form(...), password: str = Form(...)):
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return RedirectResponse(url="/login", status_code=303)
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Username already exists")


@app.get("/success", response_class=HTMLResponse)
async def success(request: Request):
    return templates.TemplateResponse("success.html", {"request": request})

# #! PARTIE CRUD ARTICLE

# Route pour afficher le formulaire de création d'article (GET)
@app.get("/articles/create", response_class=HTMLResponse)
async def create_article_form(request: Request):
    return templates.TemplateResponse("create_article.html", {"request": request})

# Route pour traiter les données du formulaire de création d'article (POST)
@app.post("/articles/create", response_class=HTMLResponse)
async def create_article(title: str = Form(...), content: str = Form(...)):
    cursor.execute("INSERT INTO articles (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    return RedirectResponse(url="/articles", status_code=303)

# Route pour afficher la liste des articles (GET)
@app.get("/articles", response_class=HTMLResponse)
async def list_articles(request: Request):
    cursor.execute("SELECT title, content , article_id FROM articles")
    articles = cursor.fetchall()
    articles_list = [{"title": article[0], "content": article[1] , "article_id": article[2]} for article in articles]
    return templates.TemplateResponse("articles_list.html", context={"request": request, "articles": articles_list})


# Route pour afficher le formulaire de modification d'article (GET)
@app.get("/articles/{article_id}/update", response_class=HTMLResponse)
async def update_article_form(request: Request, article_id: int):
    cursor.execute("SELECT title, content, article_id FROM articles WHERE article_id = ?", (article_id,))
    article = cursor.fetchone()
    print(article)
    return templates.TemplateResponse("update_article.html", context={"article": article,"request": request})

# Route pour traiter les données du formulaire de modification d'article (POST)
@app.post("/articles/{article_id}/update", response_class=HTMLResponse)
async def update_article(request: Request, article_id: int, title: str = Form(...), content: str = Form(...)):
    cursor.execute("UPDATE articles SET title = ?, content = ? WHERE article_id = ?", (title, content, article_id))
    conn.commit()
    return RedirectResponse(url="/articles", status_code=303)


# Route pour supprimer un article (GET)
@app.get("/articles/{article_id}/delete", response_class=HTMLResponse)
async def delete_article_form(request: Request, article_id: int):
    cursor.execute("SELECT title , content FROM articles WHERE article_id = ?", (article_id,))
    article = cursor.fetchone()
    return templates.TemplateResponse("delete_article.html", {"request": request, "article_id": article_id, "article": article})

@app.post("/articles/{article_id}/test", response_class=HTMLResponse)
async def test(request: Request, article_id: int, title: str = Form(...), content: str = Form(...)):
    cursor.execute("DELETE FROM articles WHERE article_id = ?", (article_id,))
    conn.commit()
    return RedirectResponse(url="/articles", status_code=303)
    



if __name__ == "__main__":
   
    uvicorn.run(app, host="localhost", port=8000)