from fastapi import FastAPI
import router
app = FastAPI()

#define endpoint
@app.get("/")
def home():
    return "Welcome Home"

app.include_router(router.router)