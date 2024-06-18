from sys import stdin

'''
4 3
1 1 2 0
2 0 1 0
3 0 1 0
4 0 0 1
'''

N,K = map(int,stdin.readline().split())
countries = list(map(lambda a: list(map(int,a.split())),stdin.readlines()))

countries.sort(key = lambda a : (-a[1],-a[2],-a[3]))

# 국가 K의 등수를 계산합니다.
rank = 1
for i in range(N):
    if countries[i][0] == K:
        print(rank)
        break
    if i < N - 1:
        if countries[i][1:] != countries[i + 1][1:]:
            rank = i + 2

