class student:
    name = "Senthil"
    def storeDetails(self): 
        self.age = 60
    def print_details(self): 
        print(self.name,end=' ')
        print(self.age)
    @staticmethod 
    def welcomeToSchool():
        print('Hey! welcome to School!!!')

class batch: 
    def __init__(self,name,number):
        self.name = name
        self.rollno = number
        
class team: 
    def __init__(self,name,rollno): 
        self.name= 'Rohan' 
        self.rollno = 5001
    def print_details(self): 
        print(self.name,end=" ")
        print(self.rollno)

s1 = student()
s1.storeDetails()
s1.welcomeToSchool()
#Student.storeDetails(s1)
s1.print_details()

b1 = batch('python',1234)
print(b1.name)
print(b1.rollno)
print(b1.__dict__)
t1 = team('Senthil',5002)
print(t1.name)
print(t1.__dict__)