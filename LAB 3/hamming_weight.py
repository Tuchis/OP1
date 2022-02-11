power = int(input())
number = 5 ** power
l = number
count = 0
Number = bin(number)
for i in range(2, len(Number)):
    Number = bin(l)
    if Number[len(Number) - 1] == "1":
        l = l >> 1
        count += 1
    else:
        l = l >> 1


if count % 2 != 0:
    print("Number ", number, " is odious number. Its hamming weight is ", count, ".", sep="")
else:
    print("Number ", number, " is evil number. Its hamming weight is ", count, "." , sep="")