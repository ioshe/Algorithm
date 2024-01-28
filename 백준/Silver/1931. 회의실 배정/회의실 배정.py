# https://www.acmicpc.net/problem/1931
from sys import stdin

conf = [list(map(int,stdin.readline().split())) for i in range(int(stdin.readline()))]
conf.sort(key=lambda x : (x[1],x[0]))

count = 0
end_time = 0

for meeting in conf:
    if meeting[0] >= end_time:
        count += 1
        end_time = meeting[1]

print(count)