import time
from datetime import datetime

import requests
from pprint import pprint

API_VACANCIES_URL: str = "https://api.hh.ru/vacancies"
PER_PAGE: int = 10
url_template = "{base_url}/?page={page}&per_page={per_page}"

page: int = 1
url = url_template.format(
    base_url=API_VACANCIES_URL,
    page=page,
    per_page=PER_PAGE
)
response = requests.get(url)
pages: int = response.json().get("pages")
print(f"Найдено: {response.json().get('found')} вакансий")
while page <= pages:
    url = url_template.format(
        base_url=API_VACANCIES_URL,
        page=page,
        per_page=PER_PAGE
    )
    response = requests.get(url)
    data = response.json()

    output: str = ""
    for item in data.get("items"):
        published_at = item.get('published_at')
        dt = datetime.fromisoformat(published_at)
        s: str = (
            f"\nНазвание: {item.get('name')}\n"
            f"Город: {item.get('area').get('name')}\n"
            f"Статус вакансии: {item.get('type').get('name')}\n"
            f"Дата публикации: {dt.strftime('%d-%m-%Y %H:%M:%S')}\n"
            f"Зарплата от: {item.get('salary', {}).get('from')} {item.get('salary', {}).get('currency')}\n\n"
            f"Ссылка: {item.get('alternate_url')}\n"
        )
        output += s
    page += 1

    with open("vacancies.txt", mode="a", encoding="UTF-8") as f:
        f.write(output)

    time.sleep(1)
