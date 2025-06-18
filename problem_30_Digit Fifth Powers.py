def SO(x):
    y=str(x)
    sum=0
    for i in range(0,int(len(y))):
        sum=sum+int(y[i])**5
    return sum

sm=0
for i in range(2,1000000):
    if i==SO(i):
        print(i)
        sm=sm+i
print("sum is",sm)