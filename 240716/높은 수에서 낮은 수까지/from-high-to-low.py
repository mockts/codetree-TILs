a, b = map(int, input().split())

if a > b:
    start, end = a, b
else:
    start, end = b, a

while start >= end:
    print(start, end=' ')
    start -= 1