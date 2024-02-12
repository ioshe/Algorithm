#https://www.acmicpc.net/problem/1966
from sys import stdin
input = stdin.readline
result = []
for _ in range(int(input().rstrip())) :
    N,m = map(int,input().rstrip().split())
    important = list(map(int,input().rstrip().split()))
    count = 1
    while True :
        # if len(important) < 2:
        #     print(count)
        #     break
        max_im = max(important)
        if max_im == important[0] :
            if m == 0 :
                result.append(str(count))
                break
            important = important[1:]
            count +=1
            m-=1
        else :
            important.append(important[0])
            important = important[1:]
            if m == 0 :
                m = len(important)-1
            else :
                m -=1
        

print("\n".join(result))