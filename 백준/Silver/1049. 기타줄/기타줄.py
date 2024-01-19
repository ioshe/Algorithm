# https://www.acmicpc.net/problem/1049

from sys import stdin

n,m = map(int,stdin.readline().split())
costs_wh_s = []
cost_re_s = []
for i in range(m) :
    a,b = list(map(int,stdin.readline().split()))
    costs_wh_s.append(a)
    cost_re_s.append(b)
cost_retail = min(cost_re_s)
cost_whole = min(costs_wh_s)
result = 0
if cost_retail*6 > cost_whole :
    result += cost_whole*(n//6)
    n = n%6
else :
    result += cost_retail*n
    n = 0

if cost_retail*n > cost_whole :
    result += cost_whole
else :
    result += cost_retail*n


print(result)