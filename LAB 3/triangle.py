start = int(input())
length = int(input())
current_length = length
for i in range(length, 0, -1):
    num = start
    for j in range(i):
        if j < i - 1:
            print(num, end=" ")
            num += 1
        else:
            print(num)