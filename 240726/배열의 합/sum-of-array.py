arr = [list(map(int, input().split())) for i in range(4)]

for i in range(4):
    sum_val = 0
    for j in range(4) :
        sum_val += arr[i][j]

    print(sum_val)