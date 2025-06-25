def common_element(a,b):
    set1=set(str(a))
    set2=set(str(b))
    inster=set1 & set2
    if len(inster)==1:
        return int(''.join(inster))
    
def istrivial(a,b):
    element=common_element(a,b)
    if element!=None and element!=0:
        list1=list(str(a))
        list2=list(str(b))
        list1.remove(str(element))
        list2.remove(str(element))
        digit1=int(''.join(list1))
        digit2=int(''.join(list2))
        if digit2:
            return (a/b==digit1/digit2,digit1/digit2)

def find_no_trivial():
    list1=[]
    mul=1
    for i in range(10,100):
        for j in range(10,100):
            if i<j and istrivial(i,j):
                bool,digit2=istrivial(i,j) 
                if bool:
                    list1.append((i,j))
                    mul*=digit2

    return list1,mul

print(find_no_trivial())
