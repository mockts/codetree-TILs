n = int(input())

for i in range(n):
    for j in range(i):
        print(' ', end=' ')
    for j in range(n - i):
        if j == n - i - 1:
            print('*', end='')
        else:
            print('* ', end='')
    print()