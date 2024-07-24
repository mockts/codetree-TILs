numbers = list(map(int, input().split()))

for i in range(1, 10):
    if numbers[i] % 3 == 0:
        print(numbers[i - 1])
        break