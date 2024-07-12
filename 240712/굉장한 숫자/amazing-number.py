# 자연수 n을 입력받습니다.
n = int(input())

# 굉장한 숫자인지를 판단하는 조건을 설정합니다.
# n이 홀수이고 3의 배수이거나, n이 짝수이고 5의 배수인 경우 굉장한 숫자로 판단합니다.
if (n % 2 != 0 and n % 3 == 0) or (n % 2 == 0 and n % 5 == 0):
    print("true")
else:
    print("false")