from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from requests import request
import apis.router.router as router
app = FastAPI()
templates = Jinja2Templates(directory="templates")
#define endpoint
@app.get("/")
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    extensions = request.query_params.get("extensions", {})
    return templates.TemplateResponse("index.html", {"request": request, "extensions": extensions})

app.include_router(router.router)