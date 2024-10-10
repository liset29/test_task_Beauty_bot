import logging
import re
from const import list_keys

Test_text = '''{name}, ваша запись изменена:
⌚️ {day_month} в {start_time}
👩 {master}
Услуги:
{services}
управление записью {record_link}'''




def find_key(text):
    stack = 0

    for char in text:
        if char == '{':
            stack += 1
        elif char == '}':
            stack -= 1
            if stack < 0:
                raise SyntaxError('Неправильная скобочная последовательность')

    if stack != 0:
       raise SyntaxError('Неправильная скобочная последовательность')


    pattern = r"\{(.*?)\}"
    keys = re.findall(pattern, text)

    for key in keys:
        if key not in list_keys:
            raise ValueError(f"Ошибка: некорректные данные - {key}")
    return text


print(find_key(Test_text))
