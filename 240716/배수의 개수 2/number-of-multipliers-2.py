count = 0

for _ in range(10):
    number = int(input())
    if number % 2 != 0:
        count += 1

print(count)