import calendar as cal
count=0
for i in range(1901,2001):
    for j in range(1,13):
        day=cal.weekday(i,j,1)
        if day==6:
            count+=1
            print(j,i, end=' ')

print(count)