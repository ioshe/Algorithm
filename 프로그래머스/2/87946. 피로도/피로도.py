visited = []
def dfs(k, dungeons, count):
    if k < 0:  # k가 0보다 작은 경우에만 탐색 중단
        return count - 1  # 마지막 던전에서 실패했으므로 count - 1 반환

    max_count = count
    for i in range(len(dungeons)):
        if i not in visited and k >= dungeons[i][0]:
            visited.append(i)
            max_count = max(max_count, dfs(k - dungeons[i][1], dungeons, count + 1))
            visited.pop()

    return max_count

def solution(k, dungeons):
    result = dfs(k, dungeons, 0)
    return result