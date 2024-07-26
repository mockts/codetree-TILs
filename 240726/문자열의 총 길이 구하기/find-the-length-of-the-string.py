# a,b = map(int, input().split())
# a,b,c = tuple(input().split())
# 위는 map(str, input().split())과 동일

# 단어가 10개면 공백은 9개
arr = input().split()

len_val = 0
for x in arr :
    len_val +=len(x)
print(len_val)


# s = input
# print(len[s]-9)