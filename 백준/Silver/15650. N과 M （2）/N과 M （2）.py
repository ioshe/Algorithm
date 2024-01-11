def dfs(visited, i, N, M, result):
    if len(visited) == M:
        result.append(visited)
        return

    for j in range(i, N + 1):
        if j not in visited:
            new_visited = visited + [j]  # Create a new path including j
            dfs(new_visited, j + 1, N, M, result)  # Pass the new path

def main():
    N, M = map(int, input().split())
    result = []
    dfs([], 1, N, M, result)
    print("\n".join(" ".join(map(str,re)) for re in result))

main()