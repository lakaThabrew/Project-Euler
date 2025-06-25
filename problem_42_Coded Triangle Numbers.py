def istriangle(n):
    n1=((1+8*n)**0.5-1)/2
    
    if n1==int(n1):
        return True
    else:
        return False

def sum(word):
    sum=0
    for i in word:
        sum+=get_pos(i)
    return sum

def get_pos(A):
    return ord(A)-ord('A')+1


file=open('0042_words.txt','r')
list1=file.read().split(',')
print(list1)
count=0
for j in list1:
    total=sum(j[1:-1])
    if istriangle(total):
        count+=1
print(count)