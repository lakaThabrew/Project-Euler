n=0
x=2
while x>0:
    for i in range(2,x):
        if x%i==0:
            break
    else:
        n=n+1
        if n==10001:
            print(x)
            break
    x=x+1