from crypt import methods
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Utilisateur fictif avec des informations d'identification
fake_user = {"username": "admin", "password": "password"}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "login_error": None})

@app.post("/user", response_class=HTMLResponse)
async def login(request: Request, username: str, password: str):
    if username == fake_user["username"] and password == fake_user["password"]:
        return RedirectResponse(url="/success")
    else:
        return templates.TemplateResponse("login.html", {"request": request, "login_error": "Invalid username or password"})

@app.get("/success", response_class=HTMLResponse)
async def success():
    return "<h1>Login successful</h1>"

@app.get("/error", response_class=HTMLResponse)
async def error():
    return "<h1>Login error</h1>"


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)