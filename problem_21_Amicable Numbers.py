def d(a):
    sum=1
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            m=i
            n=a//i
            sum=sum+m+n
    return sum

def g(a):
    if a==d(d(a)) and a!=d(a):
        n=1
    else:
        n=0
    return n

numbers=0
for k in range(2,10001):
    if g(k)==1:
        numbers=numbers+k
        print(k)
print(numbers)