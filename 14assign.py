'''#ques1
f=open("assgn.txt",'r',encoding="utf-8")
n=int(input("enter number of last lines you want to be printed"))
l=f.readlines()
l.reverse()
print(l[1:n])


#Q2
word = input("Enter word to be searched:")
k = 0
f=open("assgn.txt",'r',encoding="utf-8")
for line in f:
    words= line.split()
    for i in words:
        if (i == word):
            k = k + 1
print("Occurrences of the word:")
print(k)

#Q3
des=open("assign1.txt",'w',encoding="utf8")
src=open("assgn.txt",'r',encoding="utf8")
s=src.readlines()
for text in s:
    des.write(text)

src.close()
des.close()

#Q4
x=open("assgn.txt",encoding="utf-8")
y=open("14tassgn.txt",encoding="utf-8")
z=open("mess.txt",'w',encoding="utf-8")
x1=x.readlines()
y1=y.readlines()
for i,j in zip(x1,y1):
    z.write(i+j)
    print(i+j)

'''
#Q5
import random
i=0
x=open("new.txt",'r+')
l=[]
for i in range(10):
    l.append(random.randrange(0,100))
    l[i]=str(l[i])
print(l)
print(sorted(l))
x.writelines(l)
print(x.readlines())

