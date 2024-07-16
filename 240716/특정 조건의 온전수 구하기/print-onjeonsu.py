n = int(input())

def is_whole_number(num):
    if num % 2 == 0:
        return False
    if num % 10 == 5:
        return False
    if num % 3 == 0 and num % 9 != 0:
        return False
    return True

whole_numbers = [i for i in range(1, n + 1) if is_whole_number(i)]

print(' '.join(map(str, whole_numbers)))