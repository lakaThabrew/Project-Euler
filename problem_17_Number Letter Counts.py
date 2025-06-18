from  num2words import num2words
def f(x):
    sum=0
    for i in range(1,x):
        word=num2words(i)
        newword=''
        for j in word:
            if j!=" " and j!="-":
                newword+=j
        #print(newword)
        sum+=len(newword)
    return sum
y=f(1001)
print(y)