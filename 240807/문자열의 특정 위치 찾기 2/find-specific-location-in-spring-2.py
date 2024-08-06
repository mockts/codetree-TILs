arr = ["apple", "banana", "grape", "blueberry", "orange"]

x = input()

cnt = 0
for i in range(5):
    if x == arr[i][2] or x == arr[i][3] :
        print(arr[i])
        cnt +=1
print(cnt)