from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from app.api.router import api_router


app = FastAPI(
    title="File Analyzer"
)


app.include_router(
    api_router
)

@app.get("/")
def home():
    return {
        "message": "File Analyzer API"
    }