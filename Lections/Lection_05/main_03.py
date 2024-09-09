from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get('/')
async def root():
    logger.info('Отработал GET запрос.')
    return {'message': 'Hello, World!'}
