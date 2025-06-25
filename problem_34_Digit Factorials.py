def f(a):
    i=p=1
    while i<=a:
        p=p*i
        i=i+1
    return p

sum_f=0
sum=0
for i in range(10,1000000):
    z=str(i)
    for j in range(0,int(len(z))):
        sum_f=sum_f+f(int(z[j]))
        #print(sum_fra)
        if i==sum_f:
            print(i)
            sum=sum+i
            break
    sum_f=0
print("sum is",sum)