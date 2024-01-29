from fastapi import FastAPI, Request
import uvicorn
from logger import logger

app = FastAPI()
logger.info('Starting API...')



@app.middleware("http")
async def log_middleware(request: Request, call_next):
    log_dict = {
        'url': request.url.path,
        'method': request.method
    }
    logger.info(log_dict)

    response = await call_next(request)


@app.get("/")
async def index() -> dict:
    return {"message": "Hello world"}

@app.get("/upload-videos")
async def upload_videos() -> dict:
    return {"message": "Video Uploaded"}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)