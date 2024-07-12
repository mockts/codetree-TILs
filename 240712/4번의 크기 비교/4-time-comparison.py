a = int(input())  # 정수 a를 입력받습니다.
b, c, d, e = map(int, input().split())  # 정수 b, c, d, e를 입력받고 각각의 변수에 할당합니다.

# a가 b, c, d, e보다 큰지 여부를 판별하여 결과를 출력합니다.
print(1 if a > b else 0)
print(1 if a > c else 0)
print(1 if a > d else 0)
print(1 if a > e else 0)