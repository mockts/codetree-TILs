x = input().split()
temp = int(x[0])
x[0] = int(x[1])
x[1] = temp
print(x[0], x[1])