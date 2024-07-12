# 연도 y를 입력받습니다.
y = int(input())

# 윤년 판단 조건에 따라 true 또는 false를 출력합니다.
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print("true")
else:
    print("false")