mul=1
for x in range(1,101):
    mul=mul*x
z=str(mul)
print(mul)
y=[]
for i in range(0,int(len(z))):
    y.append(int(z[i]))
print(sum(y))