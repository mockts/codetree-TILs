s = input()

exists_ee = "No" 
exists_ab = "No"          
for i in range(len(s)- 1):
    if s[i:i+2] == 'ab':
        exists_ee = 'Yes'
    if s[i:i+2] == 'ee':
        exists_ab = 'Yes'

print(exists_ee, exists_ab)