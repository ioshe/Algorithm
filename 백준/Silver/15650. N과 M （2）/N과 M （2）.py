# https://www.acmicpc.net/problem/15650

visited = []
result = []
def dfs(i) :
    global visited
    if len(visited) == M:
        result.append(visited.copy())
        return

    while i < N+1 :
    #for i in range(1,N+1) :
        if not(visited) or i not in visited :
            visited.append(i)
            i+=1
            dfs(i)
            visited.pop()

N,M = map(int,input().split())
dfs(1)
print("\n".join(" ".join(map(str,re)) for re in result))