#ques1

class Circle:
    #r=0
    def __init__(self,radius):
        self.r=radius

    def getarea(self):
        print("area of circle is")
        x=3.14*self.r*self.r
        print(x)
    def getcircumference(self):
        print("circumference of circle is")
        y=2*3.14*self.r
        print(y)

a=Circle(5)
a.getarea()
a.getcircumference()
print('\n')

#ques2

class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display(self):
        print("name of student is "+self.name)
        print("rollno of student is "+str(self.rollno))

a=Student("hitaishi",11501078)
a.display()
print('\n')

#ques3

class Temperature:

    def celtofren(self,c):  #celsius to frenheit
        ft=c*9/5+32
        print("celsius to farenheit is "+str(ft))

    def frentocel(self,f):     #frenheit to celsius
        ct=(f-32)*5/9
        print("farenheit to celsius is "+str(ct))

h=int(input("enter c"))
i=int(input("enter f"))

x=Temperature()
x.celtofren(h)
x.frentocel(i)

'''or'''
'''class Temperature:
    def __init__(self,c,f):
        self.c=c
        self.f=f

    def celtofren(self):  #celsius to frenheit
        ft=self.c*9/5+32
        print("celsius to farenheit is "+str(ft))

    def frentocel(self):     #frenheit to celsius
        ct=(self.f-32)*5/9
        print("farenheit to celsius is "+str(ct))

h=int(input("enter c"))
i=int(input("enter f"))

x=Temperature(h,i)
x.celtofren()
x.frentocel()
'''

#ques4

class Moviedetails:
    def __init__(self,moviename,artistname,yor,ratings):
        self.moviename = moviename
        self.artistname = artistname
        self.yor = yor
        self.ratings = ratings

    def display(self):
        print("name of movie is "+self.moviename)
        print("name of artist is "+self.artistname)
        print("year of release is " +str(self.yor))
        print("ratings are "+str(self.ratings))

a=Moviedetails("veere","sonamkapoor",2018,3.5)
print("original data is")
a.display()

#to update
print("updated data is")
a.moviename="veerkiwedding"
a.artistname="kareenakapoor"
a.yor=2017
a.ratings=4

a.display()
print('\n')

#ques5

class Expenditure:
    def __init__(self,expenditure,savings):
        self.expenditure=expenditure
        self.savings=savings

    def display(self):
        print("expenditure is "+str(self.expenditure))
        print("savings are " +str(self.savings))

    def calc(self,salary,hra,ta,da):
        self.ts=salary+hra+ta+da

    def dispaly(self):
        print('total salary is '+str(self.ts))

a=Expenditure(10000,5000)
a.display()
a.calc(25000,2.5,3,2)
a.dispaly()



