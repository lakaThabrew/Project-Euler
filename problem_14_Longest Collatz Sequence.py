terms=1
for i in range(2,1000000):
    n=1
    j=i
    while j!=1:
        if j%2==0:
            j=j/2
            n=n+1
        else:
           j=3*j+1
           n=n+1   
    if n>terms:
        terms=n
        maxnumber=i
print("max is",terms)
print("max number is",maxnumber)