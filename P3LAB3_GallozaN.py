#CTI 110
#P3LAB3 - Grades and Games
#Natasha Galloza
#10/29/2024

num_grade = int(input("What is the grade (0-100):"))
letter_grade = "" #placeholder

#10pts scale
if num_grade >= 90:
    letter_grade = "A"
elif num_grade >= 80:
    letter_grade = "B"
elif num_grade >= 70:
    letter_grade = "C"
elif num_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
    

print("Your letter grade is:", letter_grade)
