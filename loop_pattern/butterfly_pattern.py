n: int = 10

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=' ')
    for q in range((n * 2) - (i * 2)):
        print(' ', end=' ')
    for k in range(i):
        print('*', end=' ')
    print()

for i in range(n - 1, 0, -1):
    for j in range(i):
        print('*', end=' ')
    for q in range((n * 2) - (i * 2)):
        print(' ', end=' ')
    for k in range(i):
        print('*', end=' ')
    print()
