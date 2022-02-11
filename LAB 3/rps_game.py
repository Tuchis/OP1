a = 0
win = ["RS", "PR", "SP"]
lose = ["SR", "RP", "PS"]
tie = ["RR", "PP", "SS"]
while a != "":
    a = input()
    if a in win:
        print("True")
    elif a in lose:
        print("False")
    elif a in tie:
        print("False | False")
    else:
        exit()
