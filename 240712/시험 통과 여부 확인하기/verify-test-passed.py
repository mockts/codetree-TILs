n = int(input())

if n >= 80:
    print("pass")
else:
    needed_score = 80 - n
    print(f"{needed_score} more score")