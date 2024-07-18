def star(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print('* ', end='')
        print()

# Example usage:
n = int(input())
star(n)