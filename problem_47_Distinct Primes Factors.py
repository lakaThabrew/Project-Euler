def f(a):
    factors=[]
    div=2
    while a!=1:
        while a%div==0:
            factors.append(div)
            a=a//div
        div+=1
    return len(set(factors))
i=100000
while True:
    if f(i)==f(i+1)==f(i+2)==f(i+3)==4:
        print(i,i+1,i+2,i+3)
        break
    i=i+1