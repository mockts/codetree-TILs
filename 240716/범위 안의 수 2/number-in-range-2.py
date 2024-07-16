total_sum = 0
count = 0

for _ in range(10):
    number = int(input())
    if 0 <= number <= 200:
        total_sum += number
        count += 1

average = round(total_sum / count, 1)

print(total_sum, average)