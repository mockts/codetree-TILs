numbers = input().split()

count = 0
total_sum = 0

for num in numbers:
    num = int(num)
    if num == 0:
        break
    if num % 2 == 0:
        count += 1
        total_sum += num

print(count, total_sum)