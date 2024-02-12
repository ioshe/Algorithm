from sys import stdin
a,*num_list = map(int,stdin.readlines())
result = []
for i in num_list :
    if i : result.append(i)
    else : result.pop()
print(sum(result))