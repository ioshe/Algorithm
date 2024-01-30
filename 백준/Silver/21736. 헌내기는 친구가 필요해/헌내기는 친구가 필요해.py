n, m = map(int, input().split())
campus = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if campus[i][j] == "I":
            start_i, start_j = i, j

move_direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
result = 0
stack = [(start_i, start_j)]

while stack:
    i, j = stack.pop()
    if campus[i][j] == "P":
        result += 1
    campus[i][j] = "X"

    for di, dj in move_direct:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and campus[ni][nj] in ["O", "P"]:
            stack.append((ni, nj))

print("TT" if result == 0 else result)