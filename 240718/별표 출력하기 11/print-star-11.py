n = int(input())
for i in range(1, n + 1):
    if i % 2 == 1:
        print('* ' * n)
    else:
        print('*   ' * (n // 2) + '* ' * (n % 2))