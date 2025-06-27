N = 20

# 2

# 3 5 7 9 ...

# 1

# 1 3 5 7 9 ...

# num = 0
# num + ((num + 1) % 2) = 1

# num = 4
# num + ((num + 1) % 2) = 5

# num = 7
# num + ((num + 1) % 2) = 7

# num ---> 4 + 1  # 1 2
# num ---> 7 + 0  # 0 3

num = 9
for i in range(num + ((num + 1) % 2), N, 2):
    print(i, end=' ')
