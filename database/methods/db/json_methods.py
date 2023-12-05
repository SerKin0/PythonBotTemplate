# todo: Чтение .json файлов
import json


def read_json_menu(menu: str, path: str = "database/data/json/keyboard_menu.json"):
    with open(path, encoding='utf-8') as f:
        return json.load(f)[menu]


def read_json(path: str):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def update_json(path: str, data=None):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)
