scores = list(map(float, input().split()))
average_score = sum(scores) / len(scores)
print(round(average_score, 1))