from sys import stdin

def dfs(N,M,nums,current,result,visited) :
    if len(current) == M :
        result.append(current)
        return 
    
    for j in range(N) :
        if visited[j] :
            continue
        else :
            visited[j] = True
            dfs(N,M,nums,current+[nums[j]],result,visited)
            visited[j] = False


N,M = map(int,stdin.readline().split())
nums = list(map(int,stdin.readline().split()))

nums.sort()

result = []
if M == 1 :
    print("\n".join(map(str,nums)))
else :
    visited = [False] * N
    for i in range(N) :
        visited[i] = True
        dfs(N,M,nums,[nums[i]],result,visited)
        visited[i] = False
    print("\n".join(" ".join(map(str,re)) for re in result))