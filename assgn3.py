# ques1

l =[]
a = int(input("enter no"))
l.append(a)
print(l)

# ques2

lo = ["google", "apple", "micro", "tesla"]
lo.append(l)
print(lo)

# ques3

li = ["hey", "you", "yes", "you"]
a = li.count("you")
print(a)

# ques4

h=[5,8,0,2]
h.sort()
print(h)

# ques5

x = [1,2,3,4]
y = [1,3,2,4]
z = x+y
z.sort()
print(z)

# ques6

list =[8,9,7,6,5]
l.append(0)
print(list)
list.pop()
print(list)

# optional

a=[]
n=int(input("enter number of elements"))
for i in range(1,n+1):
    b=int(input("enter element"))
    a.append(b)
even=[]
odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("this is even",even)
print("this is odd",odd)




