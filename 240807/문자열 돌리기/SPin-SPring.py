s = input()
L = len(s)

for i in range(L+1):
    x = s[-i:] + s[:-i]
    print(x)