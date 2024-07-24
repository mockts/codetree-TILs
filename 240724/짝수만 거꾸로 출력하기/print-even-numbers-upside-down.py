n = int(input())
numbers = list(map(int, input().split()))

even_numbers = [num for num in numbers if num % 2 == 0]
even_numbers.reverse()

print(" ".join(map(str, even_numbers)))