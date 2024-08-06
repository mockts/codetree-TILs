s, ch = input().split()
length = len(s)
start_idx = -1

for i in range(length):
    if s[i] == ch:
        start_idx = i
        break

print(start_idx)