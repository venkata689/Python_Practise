# 1) Write a program to check whether the given string present in the sequence or not.
#----------------------------------------------------
L=['digital', 'lync', 'hyderabad', 'gachibowli', 'kukatpally']
value = input("enter any String: ")
#print(value  in L)
if value in L:
    print(value ,"is presented in list")
else:
    print(value , "is not Present in list")

#2) Write a python program to perform all bitwise operations for given values:

a=45
b=65
print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(b<<2)
print(a>>2)
print(b>>2)
print(~a)
print(~b)
print(~0)

# 3) Convert the given value into integer, double, complex and calculate absolute value,
#factorial, square root, exponent of that value.
import math
z = 65.33
print(int(z))
print(float(z))
print(complex(z))
#print(double(z))
print(math.factorial(int(z)))
print(math.exp(z))
print(math.sqrt(z))
print(abs(z))


#4) Write a Python program to calculate the sum of the digits in an integer.
num = int(input("Enter the Interger : "))
sum = 0
if num >= 0:
    while (num > 0):
        rem = num%10
        sum = sum+rem
        num = num//10
    print("sum of total digits is :",sum)
else:
    print("please enter valid number")

#5) Write an program that perform all comparison operation to following two values 15 and 2?
print(15==2)
print(15!=2)
print(15<2)
print(15>2)
print(15<=2)
print(15>=2)
