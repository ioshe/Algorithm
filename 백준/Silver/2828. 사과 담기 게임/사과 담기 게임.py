from sys import stdin

N, M = map(int, stdin.readline().split())
J = int(stdin.readline())
apples = [int(stdin.readline()) for _ in range(J)]

result = 0
left = 1  # 바구니의 왼쪽 끝 위치
right = M  # 바구니의 오른쪽 끝 위치

for apple in apples:
    # 사과가 바구니 왼쪽보다 왼쪽에서 떨어질 때
    if apple < left:
        move = left - apple
        left -= move
        right -= move
        result += move
    # 사과가 바구니 오른쪽보다 오른쪽에서 떨어질 때
    elif apple > right:
        move = apple - right
        left += move
        right += move
        result += move

print(result)
