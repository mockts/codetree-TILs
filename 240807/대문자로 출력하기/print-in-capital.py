s = input()
x = ''

for i in s:
    if 'A' <= i <= 'Z':
        x += i.lower()

print(x)