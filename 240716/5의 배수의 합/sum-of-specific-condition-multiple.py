a, b = map(int, input().split())

start = min(a, b)
end = max(a, b)

total_sum = sum(i for i in range(start, end + 1) if i % 5 == 0)

print(total_sum)