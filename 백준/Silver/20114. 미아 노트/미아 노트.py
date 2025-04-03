from sys import stdin

n, h, w = map(int, stdin.readline().split())
lines = [stdin.readline().strip() for _ in range(h)]

result = []

for i in range(n):
    char = '?'
    for row in range(h):
        for col in range(i * w, (i + 1) * w):
            if lines[row][col] != '?':
                char = lines[row][col]
                break
        if char != '?':
            break
    result.append(char)

print(''.join(result))
