import json
import os

#
# data: dict[int, str] = {
#     1: 'one',
#     2: 'two',
#     3: {
#         'a': 1,
#         'b': 2
#     }
# }
# print(data)
#
# food_ratings = {"organic dog food": 2, "human food": 10}
# d = json.dumps(food_ratings)
# '{"organic dog food": 2, "human food": 10}'
#
# print(d, type(d))
# print(json.loads(d), type(json.loads(d)))

ENCODING = "UTF-8"

messages: dict[str, dict] = {
    "en": {
        "greeting": "Welcome, {name}!"
    },

    "ru": {
        "greeting": "Добро пожаловать, {name}!"
    },
}

# try:
#     with open("config34235.json", mode="r", encoding=ENCODING) as f:
#         pass
# except FileNotFoundError as err:
#     print(f"Error {err}")

if not os.path.exists("config.json"):
    raise AttributeError("Отсутсвует файл конфигураций")

with open("config.json", mode="r", encoding=ENCODING) as cf:
    config = json.load(cf)
    lang = config.get("default_settings", {}).get("language", "en")
    print(lang)
    use_logs = config.get("default_settings", {}).get("use_logs", False)
    dark_theme = config.get("dark_theme", True)

name = input()

if use_logs:
    print("[INFO] Выводится сообщение")

if dark_theme:
    print("[INFO] Темная включена")

print(
    f"{messages.get(
        lang, messages['en']
    ).get(
        'greeting'
    ).format(name=name.capitalize())}"
)
