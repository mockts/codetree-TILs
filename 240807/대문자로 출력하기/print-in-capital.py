s = input()

for c in s:
    if 'A' <= c <= 'Z' or 'a' <= c <= 'z':
        print(c.upper(), end="")