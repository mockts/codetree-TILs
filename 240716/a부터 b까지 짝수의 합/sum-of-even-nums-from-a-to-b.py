a, b = map(int, input().split())

total_sum = sum(i for i in range(a, b + 1) if i % 2 == 0)

print(total_sum)