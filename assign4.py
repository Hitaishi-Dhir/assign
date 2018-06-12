#ques 1

t=(1,'hitaishi',2,'mahak')
print(len(t))

#ques 2

s1=set([1,2,3,7,8])
print(max(s1))
print(min(s1))

#ques 3

t=(1*2*3*4)
print(t)

#ques 4(1)

s1=set([1,2,3,4])
s2=set([4,8,9,10])
s3=s1-s2
print(s3)

#4(2)
s1=set([1,2,3,4])
s2=set([3,4])
s4=s1<=s2
print(s4)
s5=s1>=s2
print(s5)

#4(3)

s3=s1&s2
print(s3)

#ques5
for i in range(1,10):
    a=input("enter name")
    b=int(input("enter marks of english"))
    c=int(input("enter marks of maths"))
    d=int(input("enter marks of physics"))
    e=int(input("enter marks of chemistry"))
    f={"name":a,"english":b,"maths":c,"physics":d,"chemistry":e}
    print("dictionary values!!")
    print(f)

#ques 6

d={"english":b,"maths":c,"physics":d,"chemistry":e}
ds=sorted(d.items())
print("sorted dictionary!!")
print(ds)

#ques 7

l=["m","i","s","s","i","s","s","i","p","p","i"]
m=l.count("m")
i=l.count("i")
s=l.count("s")
p=l.count("p")
d={"m":m,"i":i,"s":s,"i":i,"p":p}
print(d)









