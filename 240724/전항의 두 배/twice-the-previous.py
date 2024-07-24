A1, A2 = map(int, input().split())

sequence = [A1, A2]

for _ in range(8):
    next_value = sequence[-1] + 2 * sequence[-2]
    sequence.append(next_value)

print(' '.join(map(str, sequence)))