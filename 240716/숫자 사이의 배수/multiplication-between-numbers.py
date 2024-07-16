a, b = map(int, input().split())

multiples = [i for i in range(a, b + 1) if i % 5 == 0 or i % 7 == 0]

total_sum = sum(multiples)
count = len(multiples)
average = round(total_sum / count, 1) if count > 0 else 0

print(total_sum, average)