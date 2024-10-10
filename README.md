# test_task_Beauty_bot
### Описание проекта

Данный проект включает несколько задач для работы с вебхуками, JSON, MongoDB, а также проверку корректности ввода данных пользователем.

## task1 - Validation_check:
Проверяются ключи на соответствие допустимым значениям из list_keys, а также наличие открывающих и закрывающих скобок в шаблоне. Программа выводит ошибку, если формат или ключи введены некорректно.

## task2 - Counting_elements:
Программа подсчитывает количество уникальных пар [id, version] и выводит результат в формате [[id, version, count], ...]

## task3 - Difference_in_json:
Программа сравнивает значения ключей из diff_list и выводит различия только для указанных параметров.Json хранится в task3_json_files, для изменения json вставте новый json в new.json/old.json

## task4 - Clean_database
Cоздаёт документ в Mongodb, который должен быть удален через 24 часа после создания. Программа отслеживает время и удаляет документ по истечению этого срока.

## task5 - Server/Webhook 
Архитектура для обработки входящих вебхуков, которые приходят на один endpoint, но выполняют разные функции в зависимости от поля function в полученных данных.\
### Инструкция
- Запустите сервер FastAPI - uvicorn task5-Server:app 
- Перейдите и запустите файл task5-Webhook.py
- В терминале где запущен сервер выведется информация которая была передана в веб хуке

# Требования
- Python 3.x
- MongoDB 
- FastAPI