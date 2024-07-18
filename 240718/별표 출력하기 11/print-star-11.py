n = int(input())

# 패턴을 만들기 위한 두 가지 줄 모양
line1 = '* ' * n + '*'
line2 = '*   ' * n + '*'

# n * n 크기의 패턴 출력
for i in range(n):
    if i % 2 == 0:
        print(line1)
    else:
        print(line2)