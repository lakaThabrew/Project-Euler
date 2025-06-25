def isprime(a):
    if a%2==0:
        return False
    if a%3==0:
        return False
    for i in range(3,int(a**0.5)+1,2):
        if a%i==0:
            return False
    else:
        return True

def iscomposite(b):
    for i in range(3,int(a**0.5)+1,2):
        if a%i==0:
            return True
    else:
        return False

def ischris(a):
    for i in range(3,a,2):
        for j in range(1,int(a**0.5)+1):
            if a==i+2*j**2 and isprime(i)==True:
                return True
    else:
          return False
        
for a in range(999,6000,2):
    if iscomposite(a)==True and ischris(a)==False:
        print(a)
        break