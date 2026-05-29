
import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
# Import routers
from app.routers import users, study_logs

app = FastAPI()

# Ensure 'static' directory exists
if not os.path.exists('static'):
    os.makedirs('static')

# Include routers
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(study_logs.router, prefix="/study_logs", tags=["study_logs"])

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

# Optional: Mount static files if needed, but for Vercel, static files are usually handled by Vercel's build process
# app.mount("/static", StaticFiles(directory="static"), name="static")
