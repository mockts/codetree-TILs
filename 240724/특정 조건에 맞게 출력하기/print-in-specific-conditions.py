numbers = list(map(int, input().split()))

results = []
for num in numbers:
    if num == 0:
        break
    if num % 2 == 0:
        results.append(num // 2)
    else:
        results.append(num + 3)

print(' '.join(map(str, results)))