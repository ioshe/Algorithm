from sys import stdin

def dfs(N,M,re) :
    global result
    if len(re) >= M :
        result.append(re)
        return re 
    else :
        for j in range(1,N+1) :
            dfs(N,M,re + [j])

N,M = map(int,stdin.readline().split())
result= []
for i in range(1,N+1) : 
    dfs(N,M,[i])
print("\n".join(map(lambda a : " ".join(map(str,a)),result)))