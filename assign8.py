import time
import datetime
import math
import os

#ques1

'''A time tuple is a tuple is a structure with 9 values used to represent a time attribute.
The structure attribute are-
(0) tm_year
(1) tm_month
(2) tm_day
(3) tm_hour
(4) tm_minute
(5) tm_second
(6) tm_wkday
(7) tm_yday
(8) tm_isdst
'''

#ques2

print("formatted time is" +str(time.asctime()))
print('\n')

#ques3

print("extracted month from time is")
d=datetime.date.today()
print(d.month)
print('\n')

#ques4

print("extracted day from time is")
d=datetime.date.today()
print(d.day)
print('\n')

#ques5

d="11/01/2021"
m=datetime.datetime.strptime(d,"%d/%m/%Y")
print(m.date)
print('\n')

#ques6

print("local time is")
print(time.asctime(time.localtime()))
print('\n')

#ques7

n=int(input("enter number"))
fact=math.factorial(n)
print("factorial of" + str(n) +" is "+" = " +str(fact))
print('\n')

#ques8

a=int(input("enter number1"))
b=int(input("enter number2"))
print(math.gcd(a,b))

#ques9

print("current working dictionary is " +str(os.getcwd()))
print("user environment is " +str(os.environ))




