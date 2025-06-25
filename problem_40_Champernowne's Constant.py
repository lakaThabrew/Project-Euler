def d(n):
    string=''
    i=1
    while True:
        if len(string)>n+1:
            return string[n-1]
        else:
            string+=str(i)
            i+=1
print(d(1000))

X=1
mul=1
while X<=1000000:
    mul*=int(d(X))
    X*=10
print(mul)