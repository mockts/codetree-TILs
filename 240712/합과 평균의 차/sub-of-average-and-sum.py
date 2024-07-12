a, b, c = map(int, input().split())

sum = a + b + c

# 세 정수의 평균 구하기 (소수 이하를 버림)
average = sum // 3

print(sum)

print(average)

print(sum - average)