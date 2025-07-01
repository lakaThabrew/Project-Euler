def value(n):
    sum = 1
    if n == 1:
        print("The value is 1")
    else:
        for i in range(3,n+1,2):
            sum += 4*i**2 - 6*i + 6
        print("The value is", sum)
        return sum

n = int(input("Enter the number: "))
value(n)