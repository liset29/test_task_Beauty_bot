import requests

url = "http://127.0.0.1:8000/Datalore"


webhook_data = {
    "function": "function",
    "data": "Вебхук отправился успешно"}


response = requests.post(url, json=webhook_data)