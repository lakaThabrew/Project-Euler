def isabundant(n):
    sum=0
    for i in range(1,n//2+1):
        if not n%i:
            sum+=i
    if sum>n:
        return True
    else:
        return False

def check_cant_write(list,n):
    if n*2 in list:
        return False
    else:
        for i in list:
            other=n-i
            if other in list:
                return False
        else:
            return True

sum=0            
num=[]
for i in range(28124):
    if isabundant(i):
        num.append(i)
    if check_cant_write(num,i):
        sum+=i
print(sum)