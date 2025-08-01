# import json
import time
# from collections import deque
from pprint import pprint

import requests
from bs4 import BeautifulSoup
from requests import Response
from requests.exceptions import ConnectionError

# import modules_packages
# from examples import abc

url: str = "https://wallpaperscraft.ru/"

try:
    response: Response = requests.get(url)
except ConnectionError:
    print("[ERROR] Ошибка соединения...")
except Exception as err:
    print(f"Что-то пошло не так... {err}")
else:
    if response.status_code == 200:
        # print(type(response.text), type(response.content))
        # print(len(response.text), len(response.content))
        soup = BeautifulSoup(response.text, "html.parser")
        print(soup.title.text)
        categories = soup.find_all(
            "ul",
            class_="filters__list JS-Filters"
        )
        print(len(categories))

        if not categories:
            raise ValueError("Не найдены категории")

        categories, *_ = categories

        catalog: dict[str, str] = {}
        for li in categories:
            a = li.find_next("a")
            name: str = a.__dict__.get("contents")[0].strip()
            link: str = a.get("href")
            if name not in catalog:
                catalog[name] = link

        catalog.pop("дата", "default")  # существует лишний JS-url сортировки
        print("Выберите категорию:")
        idx: int = 1
        catalog_length: int = len(catalog)
        for name, link in catalog.items():
            print(f"\t {idx:>2}. {name}")

            idx += 1

        while True:
            ans: str = input("Укажите номер категории: ")
            ans = ans.strip()

            if not ans.isdigit():
                print("Ошибка, введите номер категории")
                continue

            ans: int = int(ans)
            if ans not in range(1, catalog_length + 1):
                print("Ошибка, такой номер категории несуществует")
                continue
            break

        menu: dict[int, str] = dict(enumerate(catalog, start=1))

        category: str = menu.get(ans)
        category_link: str = catalog.get(category)
        selected_category_url: str = f"{url}{category_link.lstrip()}"
        print(f"Выбрана категория '{category}' - {selected_category_url}")

        time.sleep(1)
        try:
            selected_response = requests.get(selected_category_url)
        except ConnectionError:
            print("Ошибка...")
        else:
            print(selected_response.text)
            selected_category_soup = BeautifulSoup(
                selected_response.text,
                "html.parser"
            )
    else:
        print("[ERROR] Ресурс недоступен...")
