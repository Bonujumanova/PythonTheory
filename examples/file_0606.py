n = 5

# №1
for i in range(1, n + 1, 1):
    for j in range(0, i, 1):
        ...
        print("*", end=" ")
    print()

# №2
n = 5
for i in range(1, n + 1, 1):
    for j in range(n - i):
        ...
        print(" ", end=" ")

    for k in range(i):
        ...
        print("*", end=" ")
    print()
