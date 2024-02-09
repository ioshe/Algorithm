from sys import stdin

t = int(input())
N = 40+1
fibonnacci_list = [[0,0] for i in range(N)]

fibonnacci_list[0],fibonnacci_list[1]=[1,0],[0,1]
for i in range(2,N) :
    fibonnacci_list[i][0] = fibonnacci_list[i-1][0]+fibonnacci_list[i-2][0]
    fibonnacci_list[i][1] = fibonnacci_list[i-1][1]+fibonnacci_list[i-2][1]
for i in range(t) :
    print(" ".join(map(str,fibonnacci_list[int(input())])))