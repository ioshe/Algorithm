from sys import stdin


nums = map(lambda a : list(map(int,a.split())), stdin.readlines())
size = [[0 for i in range(101)] for j in range(101)]

for x1,y1,x2,y2 in nums :
    for i in range(x1,x2) :
        for j in range(y1,y2) :
            size[i][j] = 1

print(sum(sum(si) for si in size))
