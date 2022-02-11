import math

num = float(input("Insert the number: "))
num_rounded = round(num, 3)
pi = math.pi
pi_rounded = round(pi,3)

if(num_rounded==pi_rounded):
    print("They are equal")
elif(num_rounded>pi_rounded):
    print("Number is bigger")
else:
    print("Pi is bigger")

print(num_rounded, pi_rounded)
