from sys import stdin

a = stdin.read().splitlines()
result = []
for i in a[:-1] :
    count = 0
    
    for t in i.lower() :
        if t == 'a' or t == 'e' or t == 'i' or t == 'o' or t == 'u' :
            count+=1
    result.append(count)

print("\n".join(map(str,result)))