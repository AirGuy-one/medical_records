import uvicorn
from fastapi import FastAPI

from routes import router

app = FastAPI(
    title="medical records",
    version="1.0.0"
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
