# 세 수 입력 받기
a, b, c = map(int, input().split())

# 조건 판단 후 출력
if b > a and b < c:
    print(1)
else:
    print(0)