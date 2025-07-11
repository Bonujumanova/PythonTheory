import json
import os
from pprint import pprint

file_path = os.path.join("data", "users.json")

with open(file_path, mode="r", encoding="UTF-8") as f:
    # data = f.read()
    # print(data, type(data))

    # data = json.load(f, parse_int=int, parse_float=float)
    data = json.load(f)

    for item in data:
        # address: dict = item.get("address", {}).get("geo", {}).get("lat", {})
        lat: float = item.get("address", {}).get("geo", {}).get("lat", {})
        print(lat, type(lat))

        # pprint(item.get("company"))
        pprint(item)
        break
