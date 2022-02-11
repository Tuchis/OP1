n = int(input())
sum = 0
for i in range(n+1):
    if i % 7 == 0:
        sum += i
print(sum)