s = input()

while len(s) > 1:
    for i in range(1): 
        x = int(input())
        if x >= len(s):
            x = len(s) - 1
        s = s[:x] + s[x + 1:]
        print(s)