import os

with open("example.num", mode="r", encoding="UTF-8") as file:
    # print(file.read())

    print(type(file))

    file.seek(os.SEEK_SET, os.SEEK_END)
    # file.seek(0, 2)

    curr_pos = file.tell()

    file_size = curr_pos
    print(curr_pos)

with open("example.num", mode="rb") as file:
    print(len(file.read()))

# 0 - это начало   = os.SEEK_SET
# 1 - текушая позиция     = os.SEEK_CUR
# 2 - конец файла  = os.SEEK_END
