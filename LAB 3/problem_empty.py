num = int(input())
for i in range(1, num):
    if i <= 2:
        print("*" * i)
    elif i == 3:
        print("* *")
    else:
        print("*", (i - 4) * " ", "*")
print("*" * num)