n = int(input())
grades = list(map(float, input().split()))
avg = sum(grades) / n
avg_rounded = round(avg, 1)

if avg_rounded >= 4.0:
    grade = "Perfect"
elif avg_rounded >= 3.0:
    grade = "Good"
else:
    grade = "Poor"

print(avg_rounded)
print(grade)