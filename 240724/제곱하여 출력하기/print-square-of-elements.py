n = int(input())
numbers = list(map(int, input().split()))

squared_numbers = [num ** 2 for num in numbers]

print(' '.join(map(str, squared_numbers)))