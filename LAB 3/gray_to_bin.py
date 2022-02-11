Gray_code = input()
Code = []
if Gray_code[0] == "1":
    Code.append(1)
    Bool = True
else:
    Code.append(0)
    Bool = False
Gray_code = Gray_code[1:]
for i in Gray_code:
    if i == "1":
        if Bool == True:
            Code.append(0)
            Bool = not Bool
        else:
            Code.append(1)
            Bool = not Bool
    else:
        if Bool == True:
            Code.append(1)
        else:
            Code.append(0)
for i in Code:
    print(i, sep="", end="")
print()