x=1
y=1
n=2
while x>0:
    a=[]
    z=x+y
    a=str(z)
    n=n+1
    if int(len(a))==1000:
        print(n)
        break
    x=y
    y=z