#ques1
class Animal:

    def animal_attribute(self):
        x=4
        print("no of legs are "+str(x))

class Tiger(Animal):
    landanimal = True
    def tiger_attribute(self):
        print(" ")

t=Tiger()
t.animal_attribute()
print(t.landanimal)

#ques2

a.f()=A
b.f()=B
a.g()=A
b.g()=B


#ques3

class Cop:                                     #base class making
    def __init__(self,name,age,workexp,desg):
        self.name=name
        self.age=age
        self.workexp=workexp
        self.desg=desg

    def add(self,cls):                       #add method
        cls.name=input("Name")
        cls.age=int(input("Age"))
        cls.workexp=int(input("Work exp"))
        cls.desg=input("Desg")
        return Cop(cls.name,cls.age,cls.workexp,cls.desg)

    def display(self,cls):                  #display method
        print("Nmae"+cls.name)
        print("age"+str(cls.age))
        print("workexp"+str(cls.workexp))
        print("desg"+cls.desg)

    def update(self):                       #update method
         print("updating details")
         self.add(Cop)
         self.display(Cop)

class Mission(Cop):                         #derived class

    def __init__(self,mission_details):
        self.mission_details=mission_details

    def add_mission_details(self):
        self.mission_details=input("Mission Details")
        print("")
a=Cop("hitaishi",20,1,"student")
a.add(Cop)
a.display(Cop)
a.update()
b=Mission("")
b.add_mission_details()
print('\n')


#ques4

class Shape:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b

class Square(Shape):
    def __init__(self,s):
        self.side=s

    def area(self):
        return self.side*self.side

class Rectangle(Shape):
    def __init__(self, len, bre):
        self.ln = len
        self.br = bre

    def area(self):

        return self.ln*self.br

obj=Rectangle(5,8)
obj1=Square(4)
print("area of rectangle is "+str(obj.area()))
print("area of square is "+str(obj1.area()))

