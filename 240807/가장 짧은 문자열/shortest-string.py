a = input()
b = input()
c = input()

lens = [len(a), len(b), len(c)]
max_len = max(lens)
min_len = min(lens)

print(max_len - min_len)