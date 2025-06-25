import itertools as it
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

digits='123456789'

def create(n):
    string=digits[:n]
    list1=it.permutations(string)
    list2=[''.join(i) for i in list1]
    return list2

def remove(list1):
    new=[]
    for i in list1:
        if not (i[-1] in '245680'):
            new.append(int(i))
    return sorted(new)

def prime_pandigital(list1):
    for i in range(1,len(list1)):
        if isprime(list1[-i]):
            return True,list1[-i]
    else:
        return False,0

def max():
    maxi=0
    for i in range(4,len(digits)):
        list1=create(i)
        list2=remove(list1)
        bool,n=prime_pandigital(list2)
        if bool:
            maxi=n
        
    else:
        return maxi

print(max())