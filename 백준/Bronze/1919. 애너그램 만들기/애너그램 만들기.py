#https://www.acmicpc.net/problem/1919
a = [0 for i in range(26)]
b = a[:]
for w in input() :
    a[ord(w)-ord('a')] +=1
for w in input() :
    b[ord(w)-ord('a')] +=1

c = list(map(lambda x, y: abs(x - y), a, b))
# print(c)
print(sum(c))