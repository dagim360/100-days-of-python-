student_scores = input("student list").split(", ")

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

#write your code below this line

print(max(student_scores))