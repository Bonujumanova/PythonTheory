import time

countdown: int = 3
for i in range(countdown, 0, -1):
    print(f"\r{i}", end=" ")
    time.sleep(1)

print("\rСтарт!")
