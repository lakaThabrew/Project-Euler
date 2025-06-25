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

def right_side_prime(n):
    string=str(n)
    for i in range(len(string)):
        x=int(string[i:])
        if not isprime(x):
            return False
    else:
        return True

def left_side_prime(n):
    string=str(n)
    for i in range(len(string)+1):
        x=int(string[:i+1])
        if not isprime(x):
           return False
    else:
        return True    

count=0
sum=0
x=10
while True:
    if count==11:
        print(sum)
        break
    if isprime(x):
        if left_side_prime(x) and right_side_prime(x):
            sum=sum+x
            count=count+1
    x=x+1