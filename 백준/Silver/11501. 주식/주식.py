# https://www.acmicpc.net/problem/11501

'''
input : 
3
3
10 7 6
3
3 5 9
5
1 1 3 1 2

output : 
0
10
5
'''

from sys import stdin
T = int(stdin.readline())
profits = []
for _ in range(T) :
    N = int(stdin.readline())
    prices = list(map(int,stdin.readline().split()))
    profit = 0
    temp = prices[-1]
    for i in prices[::-1][1:] :
        if i < temp :
            profit += temp - i 
        else :
            temp = i
            # print(temp,"가바뀜!")
        # print("###",i,temp,profit)
    profits.append(profit)
print("\n".join(map(str,profits)))
                