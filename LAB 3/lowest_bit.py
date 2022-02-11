num = int(input())
bit = bin(num)[2:]
ONE_pos = 0
bit_pos = 0
for i in bit:
    if i == "1":
        bit_pos += 1
        ONE_pos = bit_pos
    else:
        bit_pos += 1
print(ONE_pos)