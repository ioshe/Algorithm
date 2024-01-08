def calculate_team_score(team, S):
    score = 0
    for i in team:
        for j in team:
            if i != j:
                score += S[i][j]
    return score

def backtrack(i, n, bitmask, S, min_diff):
    if i == n:
        team1, team2 = [], []
        for j in range(n):
            if bitmask & (1 << j):
                team1.append(j)
            else:
                team2.append(j)

        score1 = calculate_team_score(team1, S)
        score2 = calculate_team_score(team2, S)
        diff = abs(score1 - score2)
        return min(min_diff, diff)

    # Assign player i to team 1
    min_diff = min(min_diff, backtrack(i + 1, n, bitmask | (1 << i), S, min_diff))

    # Assign player i to team 2
    min_diff = min(min_diff, backtrack(i + 1, n, bitmask, S, min_diff))

    return min_diff

n = int(input())
S = [list(map(int, input().split())) for _ in range(n)]

min_diff = backtrack(0, n, 0, S, float('inf'))
print(min_diff)
