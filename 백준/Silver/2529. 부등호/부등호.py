def dfs(index, result):
    # 마지막 숫자까지 탐색한 경우 결과 저장
    if index == k + 1:
        answers.append("".join(map(str, result)))
        return
    
    for num in range(10):
        if not visited[num]:  # 숫자가 이미 사용되었는지 확인
            # 부등호 조건을 만족하면 진행
            if index == 0 or (signs[index - 1] == '<' and result[-1] < num) or (signs[index - 1] == '>' and result[-1] > num):
                visited[num] = True
                result.append(num)
                dfs(index + 1, result)
                result.pop()  # 상태 복원
                visited[num] = False

# 입력 처리
k = int(input())
signs = input().split()

# 결과 저장 및 탐색
answers = []
visited = [False] * 10
dfs(0, [])

# 최대값과 최소값 출력
print(max(answers))
print(min(answers))
