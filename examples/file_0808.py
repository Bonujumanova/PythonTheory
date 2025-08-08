import json

    # with (open("js_data.txt", mode="r", encoding="UTF-8") as r_file,
    #       open("js_data.json", mode="w", encoding="UTF-8") as w_file):
    #     data = json.loads(r_file.read())
    #     print(type(data))
    #
    #     data_2 = json.dumps(data, indent=2)
    #     print(type(data_2))

from datetime import datetime
s = '2025-08-04T14:38:07+0300'

print(s)

d = datetime.fromisoformat(s)

res = d.strftime("%d-%m-%Y %H:%M:%S")

print(res)
print(type(d))
