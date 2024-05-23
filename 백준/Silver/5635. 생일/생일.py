# https://www.acmicpc.net/problem/5635

'''
5
Mickey 1 10 1991
Alice 30 12 1990
Tom 15 8 1993
Jerry 18 9 1990
Garfield 20 9 1990
'''
from sys import stdin
lines = list(map(lambda a : a.split(),stdin.readlines()[1:]))
lines.sort(key=lambda x:(int(x[3]),int(x[2]),int(x[1]))) # 일자 월자 년자
# print(lines)
print(lines[-1][0])
print(lines[0][0])
