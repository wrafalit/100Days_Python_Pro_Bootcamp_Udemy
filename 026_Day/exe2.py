import random

name = [ "Rafal", "Tomek", "Ziomek", "Alicja"]

dic = {student:random.randint(1,99) for student in name}
print(dic)

pass_student = {student:score for (student,score) in dic.items() if score > 40}
print(pass_student)
a = "teste"
print(a.split())

print("\n\n")

student_dic = {
    "student" : ["Angela", "James", "Lilly"],
    "score" : [56,76,84]
}

import  pandas

student_dic_data = pandas.DataFrame(student_dic)
print(student_dic_data)

for (index,row) in student_dic_data.iterrows():
    print(row.student == "Angela")