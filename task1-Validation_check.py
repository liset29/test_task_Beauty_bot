import logging
import re
from const import list_keys

Test_text = '''{name}, ваша запись изменена:
⌚️ {day_month} в {start_time}
👩 {master}
Услуги:
{services}
управление записью {name}'''




def find_key(text):
    stack = 0

    for char in text:
        if char == '{':
            stack += 1
        elif char == '}':
            stack -= 1
            if stack < 0:
                return 'Incorrect bracket sequence'

    if stack != 0:
       logging.error('Incorrect bracket sequence')


    pattern = r"\{(.*?)\}"
    keys = re.findall(pattern, text)

    for key in keys:
        if key not in list_keys:
            return(f"Ошибка: некорректные данные - {key} ")
    return text


print(find_key(Test_text))
