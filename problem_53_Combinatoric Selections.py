from math import factorial as f

num=0

for n in range(23,101):
    for r  in range(1,n+1):
        if f(n)/(f(r)*f(n-r))>1000000:
            #print(n,r)
            num+=1
print(num)