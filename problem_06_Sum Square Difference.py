sumofsq=0
sum=0
for i in range(1,101):
    sum=sum+i
    sumofsq=sumofsq+i**2
    #print(sum,sumofsq,sep=" ")
sqofsum=sum**2
diff=sqofsum-sumofsq
print(sqofsum,sumofsq,sep=" ")
print("diff=",diff)