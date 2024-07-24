numbers = []
input_data = input().split()

for num in input_data:
    num = int(num)
    if num == 0:
        break
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)

print(total, round(average, 1))