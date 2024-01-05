from sys import stdin

n = int(input())

li = list(map(int,stdin.readline().split()))
mapping = [[] for i in range(n)]

for index,num in enumerate(li) :
    mapping[num].append(index+1)
   
#print(mapping)
result = []
for index,room in enumerate(mapping) :
    if not(result) :
        result = room
    else :
        if isinstance(room,list) :
            room = room[::-1]
        for i in room :
            count = 0
            for re_in,num in enumerate(result) :
                if i < num :
                    count+=1
                if count == index :
                    result.insert(re_in+1,i) 
                    break

print(" ".join(map(str,result)))
