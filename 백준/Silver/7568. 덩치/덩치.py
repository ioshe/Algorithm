# https://www.acmicpc.net/problem/7568
import sys
input = sys.stdin.readline
build = []
n=int(input().rstrip())
for i in range(n) :
    build.append(list(map(int,input().rstrip().split())))
sorted(build)
result = [1]*n
# for i in range(n) :
#     for j in range(n) :
#         if build[i][0] > build[j][0] and build[i][1] > build[j][1] :
#            result[i]+=1
#         elif build[i][0] > build[j][0] or build[i][1] > build[j][1] :
#             pass
#         else :
#             result[i]+=1

for i in range(n) :
    for j in range(n) :
        if i != j :    
            if build[i][0] < build[j][0] and build[i][1] < build[j][1] :
                result[i]+=1
                

print(" ".join(map(str,result)))