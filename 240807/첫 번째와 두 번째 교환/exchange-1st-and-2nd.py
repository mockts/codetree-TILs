s = input()

a = s[0]
b = s[1]

arr = []
for i in s:
    if i == a:
        arr.append(b)
    elif i == b:
        arr.append(a)
    else:
        arr.append(i)

print(''.join(arr))