s = input()
exists = 'No'
for i in range(len(s)-1):
    if s[i:i+2] == 'ee':
        exists = 'Yes'

print(exists, end = ' ')


exists = 'No'
for i in range(len(s)-1):
    if s[i:i+2] == 'ab':
        exists = 'Yes'

print(exists, end = ' ')