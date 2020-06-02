marks=input()
marks=int(marks)
state= input()
if marks >720 or marks < 0 :
    print('invalid')
elif marks >600:
    print('government seat')
elif marks>400:
    if state == 'Tamil Nadu': 
        if marks > 500: 
            print('government seat')
        else: 
            print('private seat')
    else: 
        print('private seat')
elif marks>300:
    print('management seat')
elif marks<300:
    print('no seat')