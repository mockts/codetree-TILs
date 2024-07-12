# 중간고사 점수와 기말고사 점수 입력 받기
midterm_score, final_score = map(int, input().split())

# 중간고사 점수가 90점 이상인 경우에만 장학금을 결정
if midterm_score >= 90:
    if final_score >= 95:
        print(100000)  # 기말고사 점수가 95점 이상이면 10만 원 장학금
    elif final_score >= 90:
        print(50000)   # 기말고사 점수가 90점 이상이면 5만 원 장학금
    else:
        print(0)       # 기말고사 점수가 90점 미만이면 장학금 없음
else:
    print(0)           # 중간고사 점수가 90점 미만이면 장학금 없음