s = input()

for c in s:
    if 'A' <= c <= 'Z' or 'a' <= c <= 'z' or '0' <= c <= '9':
        if 'A' <= c <= 'Z': 
            print(c.lower(), end="")
        else: 
            print(c, end="")