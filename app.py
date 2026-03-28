from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI()

html_path = Path(__file__).parent / "templates" / "index.html"


@app.get("/hello")
async def hello():
    html_content = html_path.read_text(encoding="utf-8")
    return HTMLResponse(content=html_content)
