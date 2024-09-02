from sys import stdin

n,m = map(int,stdin.readline().split())
s = list(map(lambda a : a.strip(),stdin.readlines()))
dict_s = {a for a in s[:n]}
count = 0
for a in s[n:] :
    if a in dict_s :
        count +=1 
print(count)