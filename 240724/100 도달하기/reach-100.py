n = int(input())

first = 1
second = n
sequence = [first, second]

while True:
    next_value = first + second
    if next_value > 118:
        break
    sequence.append(next_value)
    first, second = second, next_value

print(' '.join(map(str, sequence)))