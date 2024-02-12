#https://www.acmicpc.net/problem/10814
import sys
input = sys.stdin.readline
name_list = [[] for i in range(100001)]
for _ in range(int(input().rstrip())) :
    num,name = input().rstrip().split()
    name_list[int(num)].append(name)
result = []
for i in range(100001) :
    if len(name_list[i]) :
        for j in range(len(name_list[i])) :
            result.append(str(i)+' '+name_list[i][j])
print("\n".join(result))