a, b = map(int, input().split())
sequence = [a, b]
while len(sequence) < 10:
    next_value = (sequence[-2] + sequence[-1]) % 10
    sequence.append(next_value)
print(' '.join(map(str, sequence)))