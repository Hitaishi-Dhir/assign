import numpy as np
import math

#Ques1

a=np.random.random((10,1))
print (a)
m=a.mean()
print("THE MEAN OF ELEMENTS "+str(m))
print("\n")

#Ques2

b=np.random.random((20,1))
print(b)
v=b.var()
print("VARIANCE OF ELEMENTS "+str(v))
s=b.std()
print("STANDARD DEVIATION "+str(s))
print("\n")

#Ques3

a=np.random.random((10,20))
b=np.random.random((20,25))
c=np.matmul(a,b)
print(c)
d=np.sum(c)
print(c.shape)
print("SUM OF ALL ELEMENTS "+str(d))
print("\n")

#Ques4

print("RANDOM ARRAY")
x=np.random.random((10,1))
print(x)
i=0
l=[]
for i in range(0,10):
    ans=1/(1+math.exp(-(x[i,0])))
    l.append(ans)
print("f(x)")
print(l)