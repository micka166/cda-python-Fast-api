from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
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
    cursor.execute("SELECT title, content FROM articles")
    articles = cursor.fetchall()
    articles_list = [{"title": article[0], "content": article[1]} for article in articles]
    return templates.TemplateResponse("articles_list.html", {"request": request, "articles": articles_list})


# Route pour afficher le formulaire de modification d'article (GET)
@app.get("/articles/{article_id}/update", response_class=HTMLResponse)
async def update_article_form(request: Request, article_id: int):
    cursor.execute("SELECT title, content FROM articles WHERE id = ?", (article_id,))
    article = cursor.fetchone()
    return templates.TemplateResponse("update_article.html", {"request": request, "article_id": article_id, "article": article})

# Route pour traiter les données du formulaire de modification d'article (POST)
@app.post("/articles/{article_id}/update", response_class=HTMLResponse)
async def update_article(request: Request, article_id: int, title: str = Form(...), content: str = Form(...)):
    cursor.execute("UPDATE articles SET title = ?, content = ? WHERE id = ?", (title, content, article_id))
    conn.commit()
    # Redirection vers la route pour afficher la liste des articles
    return RedirectResponse(url="/articles", status_code=303)

@app.post("/articles/delete")
async def delete_article_by_title(title: str = Form(...)):
    # Recherche de l'article par le titre
    cursor.execute("SELECT id FROM articles WHERE title = ?", (title,))
    article = cursor.fetchone()
    if article:
        article_id = article[0]  # Récupérer l'ID de l'article trouvé
        cursor.execute("DELETE FROM articles WHERE id = ?", (article_id,))
        conn.commit()
        return RedirectResponse(url="/articles", status_code=303)
    else:
        # Si aucun article correspondant au titre n'est trouvé, renvoyer une erreur
        return {"message": "Article not found"}


if __name__ == "__main__":
   
    uvicorn.run(app, host="localhost", port=8000)