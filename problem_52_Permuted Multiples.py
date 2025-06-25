def f(x):
    y1=str(x)
    y2=str(2*x)
    y3=str(3*x)
    y4=str(4*x)
    y5=str(5*x)
    y6=str(6*x)
    if len(y1)==len(y2)==len(y3)==len(y4)==len(y5)==len(y6):
        s1=set(map(int,y1))
        s2=set(map(int,y2))
        s3=set(map(int,y3))
        s4=set(map(int,y4))
        s5=set(map(int,y5))
        s6=set(map(int,y6))
        if s1==s2==s3==s4==s5==s6:
            return True
    else:
        return False

x=10000
while True:
    if f(x)==True:
        print(x)
        break
    x+=1
# Output: 142857
# Explanation: 142857, 285714, 428571, 571428,