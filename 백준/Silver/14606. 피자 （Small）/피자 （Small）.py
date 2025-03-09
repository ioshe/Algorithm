queue = [int(input())]
happy = 0

while queue:
    e = queue.pop()
    if e == 1:
        continue
    else:
        queue.append(e//2)
        queue.append(e-e//2)
        happy += e//2 * (e-e//2)

print(happy)