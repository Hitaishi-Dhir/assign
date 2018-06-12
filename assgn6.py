#ques1

i=0
while(i<10):
    num=input("enter your no")
    print("entered number is"+num)
    i=i+1

#ques2

while True:
    print("got stuck!!")

#ques3

l=[]
sq=[]
for i in range(0,5):
    num=int(input("no is"))
    l.append(num)
    print(num)
for num in l:
    a=num*num
    sq.append(a)
print(sq)

#ques4
a=[1,'hitaishi',2,'jitain',3,'neelam',4,'balwant',9.0,9.12]
inte=[]
flt=[]
str=[]
for i in a:
    if(isinstance(i,int)):
        inte.append(i)
    elif(isinstance(i,float)):
        flt.append(i)
    else:
        str.append(i)
print(inte)
print(flt)
print(str)

#ques5

l=[]
even=[]
odd=[]
for i in range(1,101):
    l.append(i)
print(l)
for i in l:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("this is even",even)
print("this is odd",odd)

#ques6

num=int(input ("enter no of rows"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end="")
    print() #for new line

#ques7

e=int(input("enter no of elements"))
for i in range(1,e):
    n=input("print your name")
    a=int(input("specify your age"))
    b=input("enter course")
    d={'name':n,'age': a,'course': b}

for j in d:
    print(j)

#ques8
l=[]
e=int(input("enter no of elements"))
for i in range(1,e):
    n=int(input("enter elements"))
    l.append(n)
print(l)
s=int(input("enter element to be searched"))
print(s)
for j in l:
    if(j==l):
        l.remove(j)
print("element deleted is"+str(j))






