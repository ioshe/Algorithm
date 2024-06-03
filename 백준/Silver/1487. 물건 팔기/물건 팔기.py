# https://www.acmicpc.net/problem/1487

'''
3
13 0
22 0
35 0
'''

from sys import stdin

n = int(stdin.readline())
buyers = list(map(lambda a : list(map(int,a.split())),stdin.readlines()))
buyers.sort(key=lambda a: a[0])
max_buyer = 0
index = 0
for i in range(n) :
    price = buyers[i][0]
    profit = 0
    for j in range(i, n):
        if price > buyers[j][1]:
            profit += (price - buyers[j][1])
    if profit > max_buyer :
        max_buyer = profit
        index = buyers[i][0]

print(index)
