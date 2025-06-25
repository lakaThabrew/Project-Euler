def isrightangled(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False
    
def generate(p):
    set1=[]
    for i in range(3,p+1):
        for j in range(4,p+1):
            c = p-i-j
            if c>i and c>j and i<j:
                if isrightangled(i,j,c):
                    set1.append([i,j,c])
    return len(set1)

def max(p):
    maximium=0
    for i in range(p+1):
        leng=generate(i)
        if leng>maximium:
            maximium=leng
            a=i
    print(a)   


max(1000)
# The code defines a function to find the maximum number of right-angled triangles
# that can be formed with a given perimeter, iterating through possible side lengths.