n = int(input())

# 위쪽 삼각형 출력
for i in range(n):
    # 공백 출력
    for j in range(i):
        print('  ', end='')
    # 별표 출력
    for j in range(2 * (n - i) - 1):
        if j == 2 * (n - i) - 2:
            print('*', end='')
        else:
            print('* ', end='')
    print()

# 아래쪽 삼각형 출력
for i in range(n - 1):
    # 공백 출력
    for j in range(n - i - 2):
        print('  ', end='')
    # 별표 출력
    for j in range(2 * (i + 2) - 1):
        if j == 2 * (i + 2) - 2:
            print('*', end='')
        else:
            print('* ', end='')
    print()