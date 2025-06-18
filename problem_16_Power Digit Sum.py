mul=1
for i in range(1,1001):
    mul=mul*2
print("2^",i,"=",mul)
z=str(mul)
x=[]
for j in range(0,int(len(z))):
    x.append(int(z[j]))
print(x)
print("sum is ",sum(x))