x=1
sum=0
while x<1000:
    if x%3==0:
        sum=sum+x
        #print(x)
    elif x%5==0:
        sum=sum+x
        #print(x)
    x=x+1
print(sum)