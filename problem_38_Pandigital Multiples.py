pandigital=['1', '2', '3', '4', '5', '6', '7', '8', '9']

def number(x):
    string=str(x)
    while True:
        for i in range(2,x):
            num=i*x
            string+=str(num)
            string_list=(sorted(list(string)))
            if string_list==pandigital:
                return True,i,string
            if len(string)>9:
                return False,0,0


for j in range(3,100000):
    stts,n,stri=number(j)
    if stts:
        print(f"number is {j} \t factor is {n} \t 9-digit string is {stri}")
    