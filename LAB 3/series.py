n = int(input())
Bool = False
number = 3
if n >= 1:
    print("1/2", end = "")
for i in range(n - 1):
    if Bool == False:
        sign = "-"
        Bool = not Bool
    else:
        sign = "+"
        Bool = not Bool

    print(" ",sign, " ",number,"/",number + 1, end = "", sep = "")
    number += 2
print()