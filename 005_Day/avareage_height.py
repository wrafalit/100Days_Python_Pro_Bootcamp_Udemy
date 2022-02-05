# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

count_weight = 0
n = 0
for s in student_heights:
  n +=1
  count_weight += s
# print(count_weight)
# print(n)
print(int(round((count_weight/n),0)))


