from sys import stdin
a = stdin.read().splitlines()

space = 0
sum = 0
for line in a :
    for i in line[space::2] :
        if i == "F" :
            sum+=1 
    space = (space+1)%2    
print(sum)