def isprime(n):
    if n==1 or n==0:
        return False
    if n==2 or n==3:
        return True
    if not n%2:
        return False
    else:
        for i in range(3,int(n**0.5)+1,2):
            if not n%i:
                return False
        else:
            return True

def makequaric(a,b):
    count=0
    n=0
    while True:
        equation=n**2 + n*a  + b
        if equation>0:
            if isprime(equation):
                count+=1
            else:
                return count
            n+=1
        else:
            return 0

def find_max():
    max=0
    for i in range(-1000,1000):
        for j in range(-1000,1000):
            count=makequaric(i,j)
            if count>max:
                max=count
                a,b,max_c=i,j,count
    return a*b,max_c

print(find_max())