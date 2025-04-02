from sys import stdin

n = int(stdin.readline())

max_name = ""
total_evolution = 0
max_evolution = -1  # 같은 진화 수 있을 때, 처음 입력된 포켓몬을 위해 -1로 시작

for _ in range(n):
    name = stdin.readline().strip()
    K, M = map(int, stdin.readline().split())

    evolution = 0
    while M >= K:
        now = M // K
        evolution += now
        M = M % K + now * 2  # 남은 사탕 + 진화 시 환급된 사탕

    if evolution > max_evolution:
        max_evolution = evolution
        max_name = name

    total_evolution += evolution

print(total_evolution)
print(max_name)