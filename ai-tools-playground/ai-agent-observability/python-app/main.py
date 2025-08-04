import logging

from fastapi import FastAPI

app = FastAPI()
logger = logging.getLogger('awesome-logger')

@app.get("/")
def read_root():
    logger.info('Accessed root endpoint')
    return {"Hello": "World"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)