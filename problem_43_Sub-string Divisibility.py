import itertools
digits="0123456789"

list1=list(itertools.permutations(digits))
def create():
    sum=0
    for j in itertools.permutations(digits):
        i=''.join(j)
        if int(i[1:4]) % 2==0 and int(i[2:5]) % 3 ==0 and int(i[3:6]) % 5==0 and int(i[4:7]) % 7==0 and int(i[5:8]) % 11==0 and int(i[6:9]) % 13==0 and int(i[7:10]) % 17==0:
            print(i)
            sum=sum+int(i)
    return sum

print(create())  