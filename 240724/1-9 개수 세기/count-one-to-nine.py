n = int(input())
elements = list(map(int, input().split()))

counts = [0] * 9

for number in elements:
    counts[number - 1] += 1

for count in counts:
    print(count)