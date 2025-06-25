digits='123456789'

def ispandigital(a,b,c):
    string=str(a)+str(b)+str(c)
    string_sorted=''.join(sorted(string))
    return string_sorted==digits

def get_couples(n):
    sum=0
    mul_list=[]
    for i in range(n):
        for j in range(n):
            if i<j:
                mul=i*j
                if ispandigital(i,j,mul):
                    print(i,j,mul)
                    if not mul in mul_list:
                        sum=sum+mul
                        mul_list.append(mul)
    return sum

print(get_couples(3000))