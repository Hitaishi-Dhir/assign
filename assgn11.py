import math
import threading
import time

#ques1

class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i

    def run(self):
         print("thread msg is",self.h)

thread1=mythread("thread is running..")
thread1.start()
time.sleep(5)
print('\n')

#ques2

class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
         time.sleep(1)
         print("the value of running thread is",self.h)
for i in range(1,11):
    thread2=mythread(i)
    thread2.start()
    thread2.join()
print('\n')

#ques3

class mythread(threading.Thread):
    def __init__(self,i,counter):
        threading.Thread.__init__(self)
        self.h=i
        self.counter=counter


    def run(self):
         time.sleep(self.counter)
         print("the value of running thread is",self.h)
         print("the value of counter is",self.counter)

l = []
e = int(input("enter no of elements"))
for i in range(1, e + 1):
    n = int(input("enter elements"))
    l.append(n)
print(l)

counter=2
for j in l:
     thread1=mythread(j,counter)
     time.sleep(counter)
     thread1.start()
     counter=counter+2
print('\n')

#ques4

class factorial(threading.Thread):

    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i

    def run(self):
        fact=math.factorial(self.h)
        print("the value of fact is",fact)

n=int(input("enter any number"))
thread2=factorial(n)
thread2.start()



