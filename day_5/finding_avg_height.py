# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

    
# Write your code below this row 👇
  sum = 0
  count = 0
  for height in student_heights:
    sum += int(height)
    count+=1

avg = round(sum/count)
print(avg)