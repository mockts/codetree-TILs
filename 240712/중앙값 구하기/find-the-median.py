# 세 개의 정수를 입력받습니다.
a, b, c = map(int, input().split())

# 세 정수를 리스트에 담습니다.
numbers = [a, b, c]

# 리스트를 오름차순으로 정렬합니다.
numbers.sort()

# 정렬된 리스트에서 중앙값을 출력합니다.
print(numbers[1])