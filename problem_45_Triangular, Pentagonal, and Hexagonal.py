tri=[x*(x+1)/2 for x in range(1,100000)]
pen=[x*(3*x-1)/2 for x in range(1,50000)]
hexa=[x*(2*x-1) for x in range(1,50000)]

for i in tri:
    if (i in pen) and (i in hexa):
        print(i)