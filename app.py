import logging
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Настройка логирования
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
templates_dir = BASE_DIR / "templates"

logger.info(f"BASE_DIR: {BASE_DIR}")
logger.info(f"templates_dir: {templates_dir}")
logger.info(f"templates_dir exists: {templates_dir.exists()}")


@app.get("/hello")
async def hello():
    logger.info("Запрос на /hello")
    hello_path = templates_dir / "hello.html"
    logger.info(f"Путь к шаблону: {hello_path}")
    logger.info(f"Шаблон существует: {hello_path.exists()}")
    html_content = hello_path.read_text(encoding="utf-8")
    logger.info(f"Шаблон загружен, размер: {len(html_content)} байт")
    return HTMLResponse(content=html_content)


@app.get("/goodbye")
async def goodbye():
    logger.info("Запрос на /goodbye")
    goodbye_path = templates_dir / "goodbye.html"
    logger.info(f"Путь к шаблону: {goodbye_path}")
    logger.info(f"Шаблон существует: {goodbye_path.exists()}")
    html_content = goodbye_path.read_text(encoding="utf-8")
    logger.info(f"Шаблон загружен, размер: {len(html_content)} байт")
    return HTMLResponse(content=html_content)
