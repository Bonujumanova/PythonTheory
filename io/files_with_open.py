# Отфильтровать имена, где 3 гласных букв

# Данные считываются из файла names.txt
# Записать данные в файл filtered_names.txt

# --------------------
# open() - функция для работы с файлами
# with - контекстный менеджер

# Режимы для работы с файлами:
# - r (read) - для чтения
# - w (write) - для записи
# - a (append) - для дозаписи
# Кодировка (желательно всегда указывать):
# UTF-8

# --------------------

CYRILLIC_VOWELS: str = "аеиоуяыэёю"

file = open(
    file="names.txt", mode="r", encoding="UTF-8"
)
# file = open("names.txt", "r", encoding="UTF-8")
# print(file, type(file))
data = file.readlines()
file.close()

result: list[str] = []
for item in data:
    _, name, _ = item.split()

    count: int = 0
    for let in CYRILLIC_VOWELS:
        curr_count = name.lower().count(let)
        count += curr_count

    if count == 3:
        result.append(name + '\n')

# ---------

file = open("filtered_names.txt", mode="w", encoding="UTF-8")
file.writelines(result)
file.close()

# print(result[:10])

# --------------------

with open(file="names.txt", mode="r", encoding="UTF-8") as r_file:
    data = r_file.readlines()

filtered_names: list[str] = []
for item in data:
    _, name, _ = item.split()

    count: int = 0
    for let in CYRILLIC_VOWELS:
        curr_count = name.lower().count(let)
        count += curr_count

    if count == 3:
        filtered_names.append(name + '\n')

with open("filtered_names_2.txt", mode="w", encoding="UTF-8") as w_file:
    w_file.writelines(filtered_names)
