for a in range(1,1000):
    for b in range(2,1000):
        c=1000-a-b
        if a<b and b<c:
            if c**2==a**2+b**2:
                print(a,b,c,sep=",")
                print("abc=",a*b*c) 