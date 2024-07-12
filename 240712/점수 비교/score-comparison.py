# A의 수학과 영어점수 입력
A_math, A_english = map(int, input().split())

# B의 수학과 영어점수 입력
B_math, B_english = map(int, input().split())

# A가 B보다 수학과 영어 점수 모두 큰지 여부 판별
if A_math > B_math and A_english > B_english:
    print(1)
else:
    print(0)