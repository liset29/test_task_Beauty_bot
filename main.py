import re

Test_text = '''{namedfs}, ваша запись изменена:
⌚️ {day_month} в {start_time}
👩 {master}
Услуги:
{services}
управление записью {record_link}'''
list_keys = ['name', 'day_month', 'day_of_week', 'start_time', 'end_time', 'master', 'services']


def find_key(text):
    stack = 0

    for char in text:
        if char == '{':
            stack += 1
        elif char == '}':
            stack -= 1
            if stack < 0:
                return False
    if stack != 0:
        return 'ошибка скобок'

    pattern = r"\{(.*?)\}"
    keys = re.findall(pattern, text)

    for key in keys:
        if key not in list_keys:
            return(f"Ошибка: некорректные данные -{key} ")


print(find_key(Test_text))
