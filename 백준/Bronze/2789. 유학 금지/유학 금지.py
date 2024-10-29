temp = input().strip()
result = []

for i in temp :
    if i not in "CAMBRIDGE" :
        result.append(i)
        
print("".join(result))