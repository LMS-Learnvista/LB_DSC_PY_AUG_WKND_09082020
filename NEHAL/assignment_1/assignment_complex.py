#Exercise 1
u = complex(3,4)
print("ID of u:",id(u))

# Exercise 2
a = complex(4,2)
b = complex(2,3)

print("2 variables are",a,"and",b )
print("Sum of a and b: ", a + b)
print("Difference of a and b: ",a - b)
print("Product of a and b: ",a * b)
print("Division of a and b: ",a / b)
print("a to the power of b: ",a ** b,"\n")

#Exercise 3
m= complex(1,2)
n= complex(2,3)
print("2 variables are",m,"and",n)
print("m is equal to n: ", m == n)
print("m is not equal to n: ", m != n,"\n")

#Exercise 4
print("Logical Operators")
print(10+20j and 20+30j)
print(0 and 20+30j)
print(20+30j and 0)
print(0 and 0,"\n")

print(10+20j and 20+30j)
print(0 or 20+30j)
print(20+30j or 0)
print(0 or 0,"\n")

print(not 10+20j)
print(not 0,"\n")

#Exercise 5
a = 10+20j
b = 10+20j
print(a is b)          
print(a is not b,"\n") 

#Exercise 6
print('2.7' in 'Python2.7.8')
print(10+20j in [10,10.20,10+20j,'Python'])
print(10+20j in (10,10.20,10+20j,'Python'))
print(30+40j in {1,20.30,30+40j})
print(30+40j in {1:100, 2.3:200, 30+40j:300})
print(10 in range(20))

