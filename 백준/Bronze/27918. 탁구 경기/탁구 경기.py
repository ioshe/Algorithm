N = int(input())
d, p = 0, 0
g_r = [input() for _ in range(N)]

for i in g_r:
    if i == "D":
        d += 1
    else:
        p += 1
    if abs(d - p) == 2:
        break

print("{}:{}".format(d, p))