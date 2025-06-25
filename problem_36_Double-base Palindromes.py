def ispalindrome(n):
    word=str(n)
    word_reverse=word[::-1]
    if word==word_reverse:
        return True
    else:
        return False

def both(n):
    bina=bin(n)
    if ispalindrome(bina[2:]) and ispalindrome(n):
        return True
    else:
        return False

def get_sum():
    sum=0
    for i in range(1,1000000):
        if both(i):
            sum+=i
    return sum

print(get_sum())