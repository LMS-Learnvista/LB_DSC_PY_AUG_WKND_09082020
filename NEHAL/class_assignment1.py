m=[]
i=0
while i < 4:
    n=[]
    j=0
    while j < 4:
        n.append(i*j)
        j += 1
    m.append(n)
    i += 1
print(m)
print("\n")

#######################

a = "*"
for i in range(5):
    print(a*i)
    i += 1
print("\n")

#######################

a = 4
for i in range(a):
    for j in range(a-i-1):
        print(end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()
