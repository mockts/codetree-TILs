from collections import defaultdict

a, b = map(int, input().split())

remainder_counts = defaultdict(int)

while a > 1:
    remainder = a % b
    remainder_counts[remainder] += 1
    a //= b

sum_of_squares = sum(count ** 2 for count in remainder_counts.values())

print(sum_of_squares)