# JSON
import json
import sys
from itertools import chain
from pprint import pprint

users: dict[int, dict] = {
    101: {
        'firstName': "Ivan",
        'lastName': "Ivanov",
        'skills': ["Python", "C#", "Java"],
    },
    145: {
        "firstName": "Petya",
        "lastName": "Petrov",
        "skills": ["Python", "Go"],
        "blocked": True,
        "additional": [float('-inf'), float('inf'), float('nan')],
        "special": None,
    }
}

# Сериализация данных
# Десериализация данных

# ----------------------------

# data, context = sys.stdin.read().split("\n\n")
# print(data.split("\n"), context.split("\n"))

data = sys.stdin.readlines()
print(data)

_, from_filename, to_filename, *data = data

with open(
        from_filename.strip(), mode="r", encoding="UTF-8"
) as r_file:
    context = r_file.read()

    _, title, *junk = data
    sys.stdout.write(title)
    sys.stdout.write(context)

    context = list(
        map(
            int, chain(*[row.split() for row in context.split("\n")])
        )
    )
    print(context)


    class A:
        pass


    length: int = len(context)
    total_sum: int = sum(context)
    temp_data = {
        "count": length,
        "positive_count": sum([1 for num in context if num >= 0]),
        "min": min(context),
        "max": max(context),
        "sum": total_sum,
        "average": round(total_sum / length, 2),
        "smile": "\U0000263A",
        A: "dfsdf"
    }
    pprint(temp_data)

to_filename = to_filename.strip()
with open(to_filename, mode="w", encoding="UTF-8") as w_file:
    *title, _ = title.split()
    sys.stdout.write(" ".join(title) + " ")
    sys.stdout.write(to_filename)

    # json.dump(temp_data, w_file, indent=4, sort_keys=True, ensure_ascii=True)
    json.dump(temp_data, w_file, indent=4, skipkeys=True)

# print(from_filename)
# print(to_filename)
# print(data)
