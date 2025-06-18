letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def calculate_value(string):
    value=0
    for i in string.lower():
        var_value=letters.index(i)+1
        value+=var_value
    return value

def read_file(filename):
    f=open(filename,'r')
    details=f.read()
    details_list=details.split(',')
    return (sorted(details_list))

y = []
try:
    y=read_file('names.txt')
except FileNotFoundError:
    print("File not found. Please ensure 'names.txt' exists in the current directory.")
sum=0

for i in y:
    length=len(i)
    position=y.index(i)+1
    value=calculate_value(i[1:length-1])
    w=value*position
    sum+=w

print(sum)