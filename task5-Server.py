from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class WebhookData(BaseModel):
    function: str
    data: str


async def function(data):
    print(data)


async def example(data):
    print(f'{data} на функцию example')


@app.post("/Datalore")
async def datalore_webhook(webhook: WebhookData):
    func = webhook.function
    data = webhook.data
    try:
        func = globals()[func]

        if callable(func):
            await func(data)
        else:
            print(f"Ошибка: {func} не является функцией.")

    except KeyError:
        print(f"Ошибка: Функция {func} не найдена.")
    except Exception as e:
        print(f"Ошибка: {e}")

# function_registry = {
#     "function": function
# }
