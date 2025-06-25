def f(a):
    return a**a
sum=0
for i in range(1,1001):
    sum=sum+f(i)
print(sum)
# The code calculates the sum of a^a for a from 1 to 1000
# and prints the result.