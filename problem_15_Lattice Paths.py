def upper(n):
    value = 1
    for i in range(n+1,2*n+1):
        value *= i
    return value

def lower(n):
    value = 1
    for i in range(1, n+1):
        value *= i
    return value

n = int(input("Enter the value of n: "))
result = upper(n) // lower(n)
print(f"The number of lattice paths in a {n}x{n} grid is: {result}")
# This code calculates the number of lattice paths in a n x n grid using combinatorial mathematics
