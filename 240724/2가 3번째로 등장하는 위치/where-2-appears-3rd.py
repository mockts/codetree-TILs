n = int(input())
numbers = list(map(int, input().split()))

positions = []

for i in range(n):
    if numbers[i] == 2:
        positions.append(i + 1)

print(positions[2])