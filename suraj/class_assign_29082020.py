#######################################
# Assignment no 1 
#######################################
print("#### Assignment No 1 ####")
print("\n")
out_list=[]
i=0
while i <=3:
    j=0
    ins_list=[]
    while j <= 3:
        ins_list.append(i*j)
        j+=1
    out_list.append(ins_list)
    i+=1
print("the list is {} {}".format(out_list,"\n" ))
#for ind in out_list:
#    print (ind)
#######################################
# Assignment no 2
#######################################
print("#### Assignment No 2 loop way ####")
print("pattern is below \n")
for i in range(4):
    for j in range(4):
        if j<=i:
            print('*',end='')
    print('')
#######################################
# Assignment no 2
#######################################
print("#### Assignment No 3 loop way ####")
print("\n")
k=6
for i in range(4):
    i+=1
    print(' '*(k-i) + '* '*i)

