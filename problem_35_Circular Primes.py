def get_rotations(n):
    rotations=[]
    digits=list(str(n))
    rotations.append(digits)
    for i in range(1,len(str(n))):
        element=digits[i:]+digits[:i]
        rotations.append(element)
    return [int(''.join(i)) for i in rotations]
   

def isprime(n):
    if n==1 or n==0:
        return False
    elif n==2 or n==3:
        return True
    elif not n%2:
        return False
    else:
        for i in range(3,int(n**0.5),2):
            if not n%i:
                return False
        else:
            return True
        

def iscircularprime(n):
    numbers=0
    rotations=get_rotations(n)
    for i in rotations:
        if isprime(i):
            numbers+=1
    if numbers==len(rotations):
        return True
    else:
        return False
    
num=13
for i in range(100,10**6):
    if isprime(i):
        if iscircularprime(i):
            num+=1
print(num)