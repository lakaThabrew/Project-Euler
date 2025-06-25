maxi=0
for a in range(2,100):
    for b in range(2,100):
        y=a**b
        list1=list(map(int,str(y)))
        sumoflist=sum(list1)
        if sumoflist>maxi:
                  maxi=sumoflist
print(maxi)