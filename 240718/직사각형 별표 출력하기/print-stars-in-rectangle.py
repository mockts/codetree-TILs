def print_rectangle_of_asterisks(n, m):
    for _ in range(n):
        print('* ' * m)


n, m = map(int, input().split())
print_rectangle_of_asterisks(n, m)