num = int(input())
multiples = []
count_5s = 0
i = 1

while count_5s < 2:
    multiple = num * i
    multiples.append(multiple)
    
    if multiple % 5 == 0:
        count_5s += 1
    
    i += 1

print(' '.join(map(str, multiples)))