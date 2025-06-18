x=[]
for a in range(2,101):
    for b in range(2,101):
        z=a**b
        x.append(z)
y=set(x)
z=list(y)
print(len(z))