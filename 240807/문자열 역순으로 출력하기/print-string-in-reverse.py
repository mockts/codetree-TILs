# x = input().strip()
# a = input().strip()
# b = input().strip()
# c = input().strip()


# words = [x, a, b, c]

words = [input() for i in range(4)]

for i in range(3, -1, -1):
    print(words[i])