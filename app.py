from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
templates_dir = BASE_DIR / "templates"


@app.get("/hello")
async def hello():
    html_content = (templates_dir / "hello.html").read_text(encoding="utf-8")
    return HTMLResponse(content=html_content)


@app.get("/goodbye")
async def goodbye():
    html_content = (templates_dir / "goodbye.html").read_text(encoding="utf-8")
    return HTMLResponse(content=html_content)
