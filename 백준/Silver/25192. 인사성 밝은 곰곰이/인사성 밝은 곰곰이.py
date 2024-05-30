# https://www.acmicpc.net/problem/25192
'''
9
ENTER
pjshwa
chansol
chogahui05
lms0806
pichulia
r4pidstart
swoon
tony9402
'''

from sys import stdin

count = 0
temp = set()
for text in map(lambda a : a.strip(),stdin.readlines()[2:]) :
    if text.strip() == "ENTER" :
        count += len(temp)
        temp = set()
        continue
    if text not in temp :
        temp.add(text)
count += len(temp)
print(count)

