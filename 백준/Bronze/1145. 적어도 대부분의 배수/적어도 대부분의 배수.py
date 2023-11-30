#https://www.acmicpc.net/problem/1145 
from itertools import combinations
from sys import stdin

my_list = [*map(int,stdin.readline().split())]

min_ = 1000001
comb = list(combinations(my_list,3))

def min_drain(a,b) :
    while b:
        a,b = b, a%b
    return a

def lcm(a,b) :
    return (a*b) // min_drain(a,b)

for a,b,c in comb :
    temp = lcm(c,lcm(a,b)) 
    if min_ > temp : 
        min_= temp

print(min_)