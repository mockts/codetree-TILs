n = int(input())
numbers = list(map(int, input().split()))

even_numbers = [num for num in numbers if num % 2 == 0]

print(' '.join(map(str, even_numbers)))