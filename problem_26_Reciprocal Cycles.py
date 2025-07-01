def no_resurive_digit(n):
    while n%2 == 0:
        n //= 2
    while n%5 == 0:
        n //= 5
    if n == 1:
        return 0
    else:
        k = 1
        r = 10 % n
        while r != 1:
            r = (r * 10) % n
            k += 1
        return k

max = 0
for i in range(1, 1000):
    k = no_resurive_digit(i)
    if k > max:
        max = i
    print(i, k)
# Output the maximum number with the longest non-recurring decimal part
print("The number with the longest non-recurring decimal part is:", max)