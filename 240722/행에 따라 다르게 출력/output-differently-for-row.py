def x(n):
    num = 1
    for row in range(1, n + 1):
        increment = 1 if row % 2 == 1 else 2
        start_num = num
        for col in range(n):
            print(start_num, end=' ')
            start_num += increment
        print()
        if row % 2 == 0:
            num += n

n = int(input())
x(n)