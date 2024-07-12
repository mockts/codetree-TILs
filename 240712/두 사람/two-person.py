# 첫 번째 사람 정보 입력 받기
info1 = input().split()
age1 = int(info1[0])
gender1 = info1[1]

# 두 번째 사람 정보 입력 받기
info2 = input().split()
age2 = int(info2[0])
gender2 = info2[1]

# 조건 판별
if (age1 >= 19 and gender1 == 'M') or (age2 >= 19 and gender2 == 'M'):
    print(1)
else:
    print(0)