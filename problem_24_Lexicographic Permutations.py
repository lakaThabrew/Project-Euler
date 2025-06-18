import itertools as it

def permucations(lists,n):
    per=list(it.permutations(lists))
    per_list=[int(''.join(i)) for i in per]
    y=sorted(per_list)
    return y[n]

digits=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
n=10**6-1
print(permucations(digits,n))