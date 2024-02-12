#https://www.acmicpc.net/problem/9461
from sys import stdin
surf_num = [1,1,1,2,2,3]
surf_len = len(surf_num)
result = []
for _ in range(int(stdin.readline())) :
    n = int(stdin.readline())
    if surf_len >= n :
        result.append(surf_num[n-1])
    else :
        for i in range(surf_len,n) :
            surf_num.append(surf_num[i-1]+surf_num[i-5])
        surf_len = n
        result.append(surf_num[n-1])
print("\n".join(map(str,result)))