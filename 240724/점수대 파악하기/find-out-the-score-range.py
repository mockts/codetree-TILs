scores = input().split()
counts = [0] * 10

for score in scores:
    score = int(score)
    if score == 0:
        break
    if 10 <= score <= 100:
        index = (score - 1) // 10
        counts[index] += 1

for i in range(10, 0, -1):
    print(f"{i * 10} - {counts[i - 1]}")