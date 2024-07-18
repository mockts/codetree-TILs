n = int(input())

for i in range(n):
    if i % 2 == 0:
        # 홀수번째 줄: 한 개의 별표 출력
        print('*')
    else:
        # 짝수번째 줄: (i + 1) 개의 별표 출력
        print('* ' * (i + 1))

# 마지막에 빈 줄 출력
print()