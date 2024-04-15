# https://www.acmicpc.net/problem/2485

from sys import stdin
import math 

# 문제의 입력방식대로 
n = int(stdin.readline())
street_trees = list(map(int,stdin.read().splitlines()))
# 가로수들의 약수들을 담을 set자료형 중복을 제거해야하기 떄문에 set을 썻다.
nums = set()

for i in range(1,n) : 
    # 가로수들이 최소로 놓일 수 있는 것은 각 가로수들의 거리의 최대공약수이다.
    # 왜 최대공약수가 쓰일까?
    nums.add(street_trees[i] - street_trees[i-1])

max_divide = None
for i in nums :
    if max_divide == None :
        max_divide = i
        continue
    max_divide = math.gcd(max_divide,i)

result = 0
for i in range(1,n) :
    temp = (street_trees[i] - street_trees[i-1])
    if temp > max_divide :
        result += temp // max_divide - 1
    # print(street_trees[i] - street_trees[i-1], max_divide, result)

print(result)