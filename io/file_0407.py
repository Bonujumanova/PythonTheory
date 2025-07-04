import sys

input()
print()

n = input()

c = 10
c = str(c)
print(c)

# ------------------------ 1

# data = sys.stdin.read()  # CTRL + D для остановки потока

# print(data.count('\n'))
# print(data.split('\n'))
# print(data.splitlines())

# data = sys.stdin.readline(1000)

data = sys.stdin.readlines()

for row in data:
    sys.stdout.write(row.strip())

nums = [1, 2, 3]
print(*nums)

for num in nums:
    # num = str(num)
    sys.stdout.write(str(num) + ' ')

# print(data, end='')

# ------------------------
import sys

lines = []
for line in sys.stdin:
    lines.append(line)
# print(lines)

sys.stdout.writelines(lines)

# ------------------------

import sys

red = int(sys.stdin.readline())
green = int(sys.stdin.readline())
blue = int(sys.stdin.readline())

total: int = (red + blue) + 1

print(total)

sys.stdout.write(f'{total}')
sys.stdout.write(str(total) + '\n')

print(total)

print('1', '2', '3')
print(1, 2, 3)
