# https://www.acmicpc.net/problem/19941

from sys import stdin

N,K = map(int,stdin.readline().split())
table = " ".join(stdin.readline()).split()

count = 0
eated = [False] * N

start = 0
end = K - 1
for i in range(N) :
    if table[i] == "P" :
        start = max(0, i - K)
        end = min(N - 1, i + K)
        
        for j in range(start,end+1) :
            if table[j] == "H" and not(eated[j]) :
                count +=1 
                eated[j] = True
                break
# print(eated)
print(count)