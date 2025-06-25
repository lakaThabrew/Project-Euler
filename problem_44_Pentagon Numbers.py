def ispentogon(n):
    x=(1+(1+24*n)**0.5)/6
    if int(x)==x:
        return True
    else:
        return False

def pentogen(n):
    return int(n/2*(3*n-1))


for i in range(1,5000):
    pi=pentogen(i)
    for j in range(i+1,5000):
        pj=pentogen(j)
        if ispentogon(pi+pj) and ispentogon(pj-pi):
            print(pi,pj,pi+pj,pj-pi)
            break