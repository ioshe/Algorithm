# https://www.acmicpc.net/problem/1302

from sys import stdin

titles = stdin.read().splitlines()[1:]

title = {}

for ti in titles :
    title[ti] = title.get(ti,0)+1

sorted_dict = dict(sorted(title.items(), key=lambda x: x[0]))
top_in,top_va = 0,0

for index,value in sorted_dict.items() :
    if value > top_va :
        top_in,top_va = index,value
    
print(top_in)