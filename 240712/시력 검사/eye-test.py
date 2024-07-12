# 두 실수 a, b를 입력받습니다.
a = float(input())
b = float(input())

# 각각의 시력이 조건에 맞는지 판단하여 결과를 출력합니다.
if a >= 1.0 and b >= 1.0:
    print("High")
elif a >= 0.5 and b >= 0.5:
    print("Middle")
else:
    print("Low")