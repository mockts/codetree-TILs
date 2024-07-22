n = int(input())


matrix = []
for i in range(1, n + 1):
    row = [i * j for j in range(1, n + 1)]
    matrix.append(row)

# 좌우 반전하여 출력합니다.
for row in matrix:
    print(' '.join(map(str, row[::-1])))