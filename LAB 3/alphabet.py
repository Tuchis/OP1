Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letter = int(input())
Letter = letter
timed_letter = letter
string = 0
string_length = 0
letter_num = 0
while timed_letter > 0:
    string += 1
    timed_letter -= string
    string_length += 1
for i in range(1, string + 1):
    delay = string_length - i
    let_num = int(i)
    if let_num > Letter:
        let_num = Letter
    while let_num > 0:
        if let_num == 1:
            print("  " * delay, Alphabet[letter_num], end = "", sep="")
        else:
            print("  " * delay, Alphabet[letter_num], " ", end = "", sep="")
        delay = 0
        letter_num += 1
        let_num -= 1
        Letter -= 1
    print()