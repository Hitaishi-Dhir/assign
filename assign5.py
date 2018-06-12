#ques1

n=int(input("enter a year"))
if(n%4==0 or n%100!=0):
    print("leap year")
else:
    print("not a leap year")

#ques2

l=int(input("enter length"))
b=int(input("enter breath"))
if(l==b):
    print("it is a square")
else:
    print("it is rectangle")

#ques3

a=int(input("enter age of 1st person"))
b=int(input("enter age of 2nd person"))
c=int(input("enter age of 3rd person"))
if(a>b and a>c):
    print("a is older")
elif(b>c):
    print("b is greater")
else:
    print("c is greater")

#ques4

n=int(input("enter points"))
if(n>=1 and n<=50):
    print("no prize")
elif(n>=51 and n<=150):
    print("wooden dog")
elif(n>=151 and n<=180):
    print("book")
elif(n>=181 and n<=200):
    print("chocolates")
else:
    print("sorry!!no prize this time")

#ques5

quantity=int(input("enter quantity"))
price=100
price=quantity*price
if(price>1000):
    cost=(price-.10*price)
    print("price is",cost)
else:
    cost=price
    print("print is",cost)
