grades = []
sum = 0
for i in range(5):
    grades.append(int(input()))
    sum += grades[i]
for i in range(5):
    if grades[i] >= 0 and grades[i] <= 100:
        continue
    else:
        print(None)
        exit()
percent_grade = round(sum / 5, 2)
if percent_grade == 0.0:
    percent_grade = 0
if percent_grade < 60:
    print("Average grade =", percent_grade, "-> F")
elif percent_grade < 67:
    print("Average grade =", percent_grade, "-> E")
elif percent_grade < 75:
    print("Average grade =", percent_grade, "-> D")
elif percent_grade < 82:
    print("Average grade =", percent_grade, "-> C")
elif percent_grade < 90:
    print("Average grade =", percent_grade, "-> B")
else:
    print("Average grade =", percent_grade, "-> A")