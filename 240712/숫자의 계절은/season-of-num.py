# 월을 입력받습니다.
m = int(input())

# 입력받은 월에 따라 계절을 판별하여 출력합니다.
if 3 <= m <= 5:
    print("Spring")
elif 6 <= m <= 8:
    print("Summer")
elif 9 <= m <= 11:
    print("Fall")
else:  # m이 12, 1, 2인 경우
    print("Winter")