n = int(input())

# 위쪽 삼각형 출력
for i in range(n):
    # 공백 출력
    for j in range(n - i - 1):
        print(' ', end=' ')
    # 별표 출력
    for j in range(2 * i + 1):
        print('*', end=' ')
    print()