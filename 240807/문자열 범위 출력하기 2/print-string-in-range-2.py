s = input()
n = int(input())

if n >= len(s):
    result = s[::-1]
else:
    result = s[-n:][::-1]

print(result)