line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
column=0
if(position[0]=="A"):
  column=0
elif(position[0]=="B"):
  column=1
else:
  column=2

if(position[1]=="1"):
  line1[column]="X"
elif(position[1]=="2"):
  line2[column]="X"
else:
  line3[column]="X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")