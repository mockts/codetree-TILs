# 정수 a를 입력받습니다.
a = int(input())

# a가 3의 배수이거나 5의 배수인지를 판별하여 결과를 출력합니다.
if a % 3 == 0 or a % 5 == 0:
    print(1)
else:
    print(0)