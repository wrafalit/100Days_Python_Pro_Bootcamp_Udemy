# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

s_max = 0
for s in student_scores:
  if s_max < s:
    s_max = s
print('The highest score in the class is: ', s_max)


