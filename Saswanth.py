marks = input()
marks = int(marks)
if marks > 100:
    print('Invalid Marks')
elif marks > 70: 
    print('First Class')
elif marks > 35: 
    print('second class')
elif marks == 35: 
    print('just pass')
else: 
    print('Failed')