from sys import stdin

n, m = map(int, stdin.readline().split())
trees = list(map(int, stdin.readline().split()))

def get_wood_length(height):
    return sum(tree - height if tree > height else 0 for tree in trees)

bottom, top = 0, max(trees)
result = 0

while bottom <= top:
    mid = (bottom + top) // 2
    cut = get_wood_length(mid)

    if cut >= m:
        result = mid
        bottom = mid + 1
    else:
        top = mid - 1

print(result)
