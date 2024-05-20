# https://www.acmicpc.net/problem/1652

'''
5
....X
..XX.
.....
.XX..
X....
'''

from sys import stdin
n = int(stdin.readline())
text = stdin.readlines()
max_wid = 0
for i in text :
    max_wid += sum([1 for num in (len(j) for j in i.strip().split("X")) if num >= 2])

max_hei = 0 
for i in zip(*text) :
    max_hei += sum([1 for num in (len(j) for j in "".join(i).strip().split("X")) if num >= 2])
print(max_wid, max_hei)
