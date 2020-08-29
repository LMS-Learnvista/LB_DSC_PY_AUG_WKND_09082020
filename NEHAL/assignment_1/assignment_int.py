#Exercise 1
A = 10
print(type(A),"\n")

#Exercise 2
x = 20
y = 20

print("ID of x:",id(x))
print("ID of y:",id(y),"\n")

#Exercise 3
u = 300
v = 300

print("ID of u:",id(u))
print("ID of v:",id(v),"\n")

# Exercise 4
a = 40
b = 20

print("2 variables are",a,"and",b )
print("Sum of a and b: ", a + b)
print("Difference of a and b: ",a - b)
print("Product of a and b: ",a * b)
print("Division of a and b: ",a / b)
print("Remainder after dividing a and b: ",a % b)
print("Quotient after dividing a and b: ",a // b)
print("a to the power of b: ",a ** b,"\n")

#Exercise 5
m = 5
n = 15

print("2 variables are",m,"and",n)
print("m is greater than n: ", m > n)
print("m is smaller than n: ", m < n)
print("m is greater than or equal to n: ", m >= n)
print("m is less than or equal to n: ", m <= n,"\n")

#Exercise 6
print("2 variables are",m,"and",n)
print("m is equal to n: ", m == n)
print("m is not equal to n: ", m != n,"\n")

#Exercise 7
print("Logical Operators")
print(10 and 20)
print(0 and 20)
print(20 and 0)
print(0 and 0,"\n")

print(10 or 20)
print(0 or 20)
print(20 or 0)
print(0 or 0,"\n")

print(not 10)
print(not 0,"\n")

#Exercise 8
print("Bitwise Operators")
print(10 & 20)
print(10 | 20)
print(10 ^ 20)
print(~ 10)
print(10 << 2)
print(10 >> 2,"\n")

#Exercise 9
a = 10
b = 10
print(a is b)          
print(a is not b,"\n") 

a = 1000
b = 1000
print(a is b)          
print(a is not b,"\n")

#Exercise 10
print(10+(10*32)//2**5&20+(~(-10))<<2)
print("\n")

#Exercise 11
print('2' in 'Python2.7.8')
print(10 in [10,10.20,10+20j,'Python'])
print(10 in (10,10.20,10+20j,'Python'))
print(2 in {1,2,3})
print(3 in {1:100, 2:200, 3:300})
print(10 in range(20),"\n")

#Exercise 12
x = 9876
print(bin(x))
print(oct(x))
print(hex(x),"\n")

#Exercise 13
a = 0b1010000
print(a)

b = 0o7436
print(b)

c = 0xfade
print(c)

print(bin(80))

print(oct(3870))

print(hex(64222))

print(bin(0b1010000))

print(bin(0xfade))

print(oct(0xfade))

print(oct(0o7436))

print(hex(0b1010000))

print(hex(0xfade))

