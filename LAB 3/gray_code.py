code = input()
num = "0b" + code
Code = int(num, base = 2)
print(Code)
code_ex = Code >> 1
gray_code = Code ^ code_ex
Gray_code = bin(gray_code)[2:]
while len(Gray_code) != len(code):
    Gray_code = "0" + Gray_code
print(Gray_code)