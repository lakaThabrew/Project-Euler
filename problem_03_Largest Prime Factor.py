x=2
while x<=600851475143:
    if 600851475143%x==0:
        for i in range(2,x):
            if x%i==0:
                break
        else:
            print(x)
    x=x+1