n = int(input()) 

s = 0
while n > 0:
    s += n % 10
    n //= 10

s_str = str(s)

cnt = 0
for i in s_str:
    if i == '1':
        cnt += 1

print(cnt)