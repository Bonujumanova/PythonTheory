# n: int = 13
#
# for i in range(1, n, 2):
#     for j in range(n // 2 + 1 - i):
#         if i <= n // 2 + 1:
#             print('*', end=' ')
#         else:

n: int = 9
for i in range(n + ((n + 1) % 2), 0, -2):
    for _ in range(i):
        print('*', end=' ')
    for _ in range(0):
        pass

    print()
