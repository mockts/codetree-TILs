numbers = list(map(int, input().split()))

for i in range(3, len(numbers)):
    if numbers[i] == 0:
        print(sum(numbers[i-3:i]))
        break