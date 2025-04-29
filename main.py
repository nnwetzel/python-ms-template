from fastapi import FastAPI
import uvicorn
from util.config import get_config

app = FastAPI()

@app.get('/health')
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    config = get_config()
    uvicorn.run("main:app", host=config.NLP_SERVICE_HOST, port=int(config.NLP_SERVICE_PORT), reload=False)