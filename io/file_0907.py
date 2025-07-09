import sys

with open("example_0907.txt", mode="w", encoding="UTF-8") as f:
    data = sys.stdin.readlines()

    f.writelines(data)
