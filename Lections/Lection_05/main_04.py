from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.post('/items/')
async def creat_item(item: Item):
    logger.info('Отработал POST запрос.')
    return item
