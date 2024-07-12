# 성별을 입력받습니다.
gender = int(input().strip())

# 나이를 입력받습니다.
age = int(input().strip())

# 성별과 나이에 따라 상황을 판단하여 출력합니다.
if gender == 0:
    if age >= 19:
        print("MAN")
    else:
        print("BOY")
elif gender == 1:
    if age >= 19:
        print("WOMAN")
    else:
        print("GIRL")