numbers = []
input_data = input().split()

for num in input_data:
    if num == '0':
        break
    numbers.append(num)

print(' '.join(numbers[::-1]))