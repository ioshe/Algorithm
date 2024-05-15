# https://www.acmicpc.net/problem/2847

'''
input :
4
5
3
7
5

output :
6
'''
       
from sys import stdin

nums = list(map(int,stdin.readlines()[1:]))


def calculate_decreases(scores):
    n = len(scores)
    decreases = 0

    # 역순으로 점수를 검토
    for i in range(n - 2, -1, -1):
        if scores[i] >= scores[i + 1]:
            decreases += scores[i] - (scores[i + 1] - 1)
            scores[i] = scores[i + 1] - 1

    return decreases

print(calculate_decreases(nums))
