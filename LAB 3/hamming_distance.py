x, y = input().split()
x, y = int(x), int(y)
x, y = bin(x), bin(y)
count = 0
for i in range(2, len(x)):
    if x[i] != y[i]:
        count += 1
print(count)