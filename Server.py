from fastapi import FastAPI
from pydantic import BaseModel

from const import function_registry

app = FastAPI()


class WebhookData(BaseModel):
    function: str
    data: str

async def function(data):
    print(data)


@app.post("/Datalore")
async def datalore_webhook(webhook: WebhookData):
    func = webhook.function
    data = webhook.data
    try:
        func = function_registry[func]
        await func(data)
    except Exception as e:
        print(f'Ошибка: {e}')
