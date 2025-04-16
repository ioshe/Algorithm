# https://www.acmicpc.net/problem/14247

from sys import stdin

# 산에는 n개의 나무가 있는데
# 하루에 한 나무씩 n일 산에 오르며 나무를 자른다.
# 나무의 처음 길이와 하루에 자라는 양이 주어졌을 때, 영선이가 얻을 수 있는 최대 나무양
# 자른 이후에도 나무는 0부터 다시 자라기 때문에 같은 나무를 여러 번 자를 수는 있다.

'''
5
1 3 2 4 6
2 7 3 4 1
'''

n = int(stdin.readline())
trees = list(map(int, stdin.readline().split()))
grows = list(map(int, stdin.readline().split()))
result = 0




order = []
for i in range(n):
    order.append([trees[i], grows[i]])

order.sort(key=lambda x: (x[1], x[0]))

# print(order)
for i in range(n):

    result += order[i][0] + (order[i][1] * i)

print(result)
