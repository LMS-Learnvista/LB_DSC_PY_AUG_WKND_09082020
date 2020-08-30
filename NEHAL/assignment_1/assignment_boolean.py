#Exercise 1
x = True
print("ID of x:",id(x))


#Exercise 2
u = 1
v = 0

print("ID of u:",id(u))
print("ID of v:",id(v),"\n")

# Exercise 3
a = True
b = False

print("2 variables are",a,"and",b )
print("Sum of a and b: ", a + b)
print("Difference of a and b: ",a - b)
print("Product of a and b: ",a * b)
print("Division of a and b: ",b / a)
print("Remainder after dividing a and b: ",b % a)
print("Quotient after dividing a and b: ",b // a)
print("a to the power of b: ",a ** b,"\n")

#Exercise 4
m = True
n = False

print("2 variables are",m,"and",n)
print("m is greater than n: ", m > n)
print("m is smaller than n: ", m < n)
print("m is greater than or equal to n: ", m >= n)
print("m is less than or equal to n: ", m <= n,"\n")

#Exercise 5
print("2 variables are",m,"and",n)
print("m is equal to n: ", m == n)
print("m is not equal to n: ", m != n,"\n")

#Exercise 6
print("Logical Operators")
print(True and True)
print(False and True)
print(True and False)
print(False and False,"\n")

print(True or True)
print(False or True)
print(True or False)
print(False or False,"\n")

print(not True)
print(not False,"\n")

#Exercise 7
print("Bitwise Operators")
print(10 & 20)
print(10 | 20)
print(10 ^ 20)
print(~ 10)
print(10 << 2)
print(10 >> 2,"\n")

#Exercise 8
a = True
b = True
print(a is b)          
print(a is not b,"\n") 

a = False 
b = False
print(a is b)          
print(a is not b,"\n")

#Exercise 9
print(True in [10,10.20,10+20j,'Python', True])
print(False in (10,10.20,10+20j,'Python', False))
print(True in {1,2,3, True})
print(True in {True:100, False:200, True:300})
print(False in {True:100, False:200, True:300})

