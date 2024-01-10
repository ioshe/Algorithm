#https://www.acmicpc.net/problem/15649
# n과 m을 입력받습니다.
n, m = list(map(int, input().split())) 

# s는 현재까지 생성된 수열을 저장합니다.
s = []

# result는 최종적으로 생성된 모든 수열을 저장합니다.
result = []

# 깊이 우선 탐색(DFS) 함수를 정의합니다.
def dfs():
    # 만약 s의 길이가 m과 같다면, s를 결과에 추가합니다.
    if len(s) == m:
        result.append(" ".join(map(str, s)))
        return
    
    # 1부터 n까지의 숫자를 순회합니다.
    for i in range(1, n + 1):
        # 만약 i가 s에 없다면, 즉 아직 방문하지 않았다면
        if i not in s:
            s.append(i) # s에 i를 추가합니다.
            dfs()       # 새로운 수열을 생성하기 위해 dfs를 재귀 호출합니다.
            s.pop()     # s에서 마지막 요소를 제거하여 다른 수열을 생성할 준비를 합니다.

# 깊이 우선 탐색을 시작합니다.
dfs()

# 생성된 모든 수열을 출력합니다.
print("\n".join(result))
