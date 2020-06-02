print('Enter the marks of the Student')
marks = int(input())

if marks > 90: 
    Grade = 'S'
elif marks > 80: 
    Grade = 'A'
elif marks > 70: 
    Grade = 'B'
elif marks > 60: 
    Grade = 'C'
elif marks > 50: 
    Grade = 'D'
elif marks > 35: 
    Grade = 'E'
else: 
    Grade='F'

print("Student's Grade is : " ,Grade)
