from pprint import pprint
import sys

with open("example_0907.txt", mode="w", encoding="UTF-8") as f:
    data = sys.stdin.readlines()

    f.writelines(data)

with open("translators_base.txt", mode="r", encoding="UTF-8") as f:
    pprint(f.readlines())
