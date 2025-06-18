for i in range(1,10000000000):
    for x in range(1,21):
        if i%x!=0:
            break
    else:
        print(i)
        break