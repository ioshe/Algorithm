#https://www.acmicpc.net/problem/1158
from collections import deque
n,k = map(int,input().split())
cnt = 1
yose = deque(range(1,n+1))
result= []

while yose :
    if cnt % k == 0 :
        result.append(yose.popleft())
    else :
        yose.append(yose.popleft())
    cnt +=1

print(f'<{", ".join(map(str,result))}>')