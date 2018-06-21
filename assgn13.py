#ques1

a=3
try:
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print(" ZERO DIVISION ERROR")
print('\n')

#ques2

try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print(" INDEX ERROR")
print('\n')

#ques3

'''
try:
    raise NameError("Hi there")  
except NameError as e:
    print("An exception")
    raise
'''
print("OUTPUT IS")
print("'AN EXCEPTION'")
print('\n')

#ques4
'''
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
		print(c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
'''
print("OUTPUT OF FIRST FUNCTINAL CALL IS")
print(-5.0)
print("OUTPUT OF SECOND FUNCTINAL CALL IS")
print("a/b result is 0")
print('\n')

#quse5

#value error
try:
    a=int(input("enter valid no"))

except ValueError:
    print("please enter integer")
else:
    print(a)
finally:
    print("i ll execute whether exception occurs or not")
print("")

#indexerror
try:
    l=[1,2,3]
    print(l[6])
except IndexError:
    print("please enter list element")
print("")

#import error

try:
    import articulate
except ImportError:
    print("error there its not in lib")
else:
    print("exists")
print('\n')

#ques6

class AgeTooSmallError(Exception):
    pass
a=0
while a<18:
    try:
        a = int(input("ENTER AGE"))
        if a<18:
            raise AgeTooSmallError
            pass
        else :
            print("APPROPRIATE GO AHEAD!",a)
    except:
        print("AGE LESS THAN 18 ")
