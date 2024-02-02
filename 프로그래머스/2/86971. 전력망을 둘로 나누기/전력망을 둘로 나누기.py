def solution(n, wires):
    global graph 
    graph = {i : [] for i in range(1,n+1)}
    for (i,j) in wires :
        graph[i].append(j)
        graph[j].append(i)
    
    print(graph)
    #print(dfs(1,[3]),dfs(3,[1]))
    min = 100
    for (one,two) in wires :
        v1 = dfs(one,[two])
        v2 = dfs(two,[one])
        temp = abs(v1-v2)
        if v1 == 1 or v2 == 1 :
            temp -=1
        if temp < min :
            min = temp
    answer = min
    return answer

def dfs(start,visited) :
    global graph
    for i in graph[start] :
        if i not in visited :
            visited.append(i)
            dfs(i,visited)
    #print(visited)
    return len(visited)     
            