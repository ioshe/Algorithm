# https://www.acmicpc.net/problem/17269

from sys import stdin

strokes = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

N,M = map(int,stdin.readline().split())
A,B = map(lambda a : a.strip(), stdin.readline().split())

if len(A) > len(B) :
    B+= (len(A) - len(B)) * " "
else :
    A+= (len(B) - len(A)) * " "

temp = [strokes[ord(j)-ord('A')] for i in list(zip(A,B)) for j in i if j != " "]

while len(temp) > 2:
    temp = [(temp[i]+temp[i+1])%10 for i in range(len(temp)-1)]
    
print(f'{int("".join(map(str,temp)))}%')