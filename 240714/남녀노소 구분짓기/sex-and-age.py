sex = int(input())
age = int(input())

if sex == 0 and age>= 19:
    print("MAN")
elif sex == 1:
    print("WOMAN")

if sex == 1 and age<= 19:
    print("BOY")
elif sex == 1:
    print("GIRL")