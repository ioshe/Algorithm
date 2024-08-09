def min_cut_chocolate(N, M):

    # N * M 크기의 초콜릿을 1 * 1 크기로 만들기 위해 필요한 최소 쪼개기 횟수 계산

    return N * M - 1

# 입력 받기

N, M = map(int, input().split())

# 결과 출력

print(min_cut_chocolate(N, M))

