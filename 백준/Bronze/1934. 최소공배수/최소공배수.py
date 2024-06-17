# https://www.acmicpc.net/problem/1934

'''
3
1 45000
6 10
13 17
'''

from sys import stdin

def lcd(a,b) :
    if a < b : a,b = b,a
    while b > 0 :
        a,b = b,a%b
    return a
n = int(stdin.readline())
nums = list(map(lambda a : list(map(int,a.split())),stdin.readlines()))

for a,b in nums :
    print(a*b // lcd(a,b))