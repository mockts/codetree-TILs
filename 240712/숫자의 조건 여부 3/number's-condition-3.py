# 정수 a를 입력받습니다.
a = int(input())

# a가 13의 배수이거나 19의 배수인지를 판단하여 결과를 출력합니다.
if a % 13 == 0 or a % 19 == 0:
    print(True)
else:
    print(False)