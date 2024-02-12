#https://www.acmicpc.net/problem/1476
import sys
input = sys.stdin.readline

correct= list(map(int,input().rstrip().split()))
#(1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)
result = 1
if sum(correct) == 3:
        print(1)
        exit()
if correct[0] == 15 :
    correct[0] -= 15
if correct[1] == 28 :
    correct[1] -= 28
if correct[2] == 19 :
    correct[2] -= 19

while True :
    if result%15==correct[0] and result%28==correct[1] and result%19 == correct[2] :
        print(result)
        break
    result +=1