from sys import stdin

n = int(stdin.readline())
min_result = []

def compare(mbti1, mbti2):
    return sum(c1 != c2 for c1, c2 in zip(mbti1, mbti2))

def dfs(start,size,mbtis,visited,make):
    if len(visited) == 3 :
        make.append(visited)
        return 
    for i in range(start,size) :
        dfs(i+1,size,mbtis,visited+[mbtis[i]],make)
    return make
result = []
for i in range(n) :
    m = int(stdin.readline())
    mbtis = list(stdin.readline().rstrip().split())
    if m > 32 :
        result.append(0)
    else :
        low = 1000
        make = dfs(0,m,mbtis,[],[])
        #print(make)
        for combo in make :
            distance = compare(combo[0], combo[1]) + compare(combo[1], combo[2]) + compare(combo[0], combo[2])
            if low > distance :
                low = distance
        result.append(low)
print("\n".join(map(str,result)))