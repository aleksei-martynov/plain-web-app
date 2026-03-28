from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

templates_dir = Path(__file__).parent / "templates"


@app.get("/hello")
async def hello():
    html_content = (templates_dir / "hello.html").read_text(encoding="utf-8")
    return HTMLResponse(content=html_content)


@app.get("/goodbye")
async def goodbye():
    html_content = (templates_dir / "goodbye.html").read_text(encoding="utf-8")
    return HTMLResponse(content=html_content)
