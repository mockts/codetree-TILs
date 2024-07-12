# 정수 a 입력받기
a = int(input().strip())

# 주어진 규칙에 따라 계산
if a % 2 == 0:
    result = a // 2
else:
    result = (a + 1) // 2

# 최종 결과 출력
print(result)