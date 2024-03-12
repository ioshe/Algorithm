from sys import stdin

def bfs(start, n):
    global graph
    queue = [start]  # 시작 노드를 큐에 직접 추가
    visited = [0] * n
    # visited[start] = 1
    
    idx = 0
    while idx < len(queue):
        current = queue[idx]
        idx += 1
        for next_node in graph[current]:
            if not visited[next_node]:
                visited[next_node] = 1
                queue.append(next_node)

    return visited

n = int(stdin.readline())
nums = map(lambda a : list(map(int,a.split())),stdin.read().splitlines())
graph = {i: [] for i in range(n)}
for i_idx, i in enumerate(nums):
    for j_idx, j in enumerate(i):
        if j == 1:
            graph[i_idx].append(j_idx)

# print(graph)

result = []
for i in range(n) :
    result.append(bfs(i, n))

print("\n".join(" ".join(map(str,r)) for r in result))


