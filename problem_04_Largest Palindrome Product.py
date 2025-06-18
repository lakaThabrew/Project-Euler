max=0
for x in range(101,1000):
    for y in range(101,1000):
        z=str(x*y)
        if len(z)%2==0:
            a1=[]
            a2=[]
            h1=z[0:int(len(z)/2)]
            h2=z[int(len(z)/2):]
            for i in range(-1,-4,-1):
                a1.append(h2[i])
            for j in range(0,3):
                a2.append(h1[j])
            if a1==a2:
                m=int(z)
                if m>max:
                    print(m)
                    max=m