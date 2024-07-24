N = int(input())
numbers = list(map(int, input().split()))

min_value = min(numbers)
count_min_value = numbers.count(min_value)

print(min_value, count_min_value)