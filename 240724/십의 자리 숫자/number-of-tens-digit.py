inputs = input().split()
counts = [0] * 9

for num in inputs:
    if num == '0':
        break
    number = int(num)
    if number >= 10:
        tens_digit = number // 10
        counts[tens_digit - 1] += 1

for i in range(9):
    print(f"{i + 1} - {counts[i]}")