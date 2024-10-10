import json
from const import diff_list

with open('task3_json_files/old.json', 'r', encoding='utf-8') as file:
    old_json = json.load(file)

with open('task3_json_files/new.json', 'r', encoding='utf-8') as file:
    new_json = json.load(file)


def find_difference_in_json(old_json, new_json):
    result = {}

    for key in old_json:
        if key in diff_list and old_json[key] != new_json[key]:
            result[key] = new_json[key]
        if isinstance(old_json[key], dict) and isinstance(new_json[key], dict):
            check = find_difference_in_json(old_json[key], new_json[key])
            result.update(check)
        if isinstance(old_json[key], list) and isinstance(new_json[key], list) and old_json[key] != new_json[key] and key in diff_list:
            result[key] = new_json[key]

    return result


result = find_difference_in_json(old_json, new_json)
print(f'Result = {result}')
