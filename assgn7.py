#ques1

r=int(input("enter radius"))
def area():
   return 3.14*r*r
a=area()
print(a)

#ques2

def perfect(n):
    sum = 0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if(sum==n):
            return True
    else:
            return False
for i in range(1,1001):
    if(perfect(i)):
        print(i)

#ques3

def table(num,i=1):
    if(i<=10):
        print("table of "+str(n) +" is "+str(n)+"*"+str(i)+"="+str(num*i))
        table(n,i+1)
    else:
        return 0
n=int(input("enter num"))
table(n,1)

#ques4

def power(a,b):
    if(b==1):
        return a
    else:
        return pow(a,b)
r=power(4,2)
print(r)

#ques5

def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
num=int(input("enter number"))
a=fact(num)
print("factorial of "+ str(num) +" is "+"= "+ str(a))
dict={num:a}
dict.update({num:a})
print("num : value is"+str(dict))





