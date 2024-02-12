#https://www.acmicpc.net/problem/3085
def cal_board(board) :
    l = len(board)
    end = False
    t_sum = 0
    for i in range(l-1) : #제일 바깥 루프
        sum = 1
        for j in range(i+1,l) : #i 값을 기준으로 +1이 맞는지
            if board[i] != board[j] : #아니라면 계산 된 범위까지 i를 옮김
                i=j-1
                break
            else :
                sum+=1 
    
        t_sum=max(sum,t_sum)
    return t_sum

def verti_change(a,b,col) : #세로
    board[a][col],board[b][col] = board[b][col],board[a][col]
def hori_change(a,b,row) : #가로
    board[row][a],board[row][b] = board[row][b],board[row][a]

import sys
input = sys.stdin.readline
max_ = 0
board = []
for n in range(int(input().rstrip())) :
    board.append(list(input().rstrip()))

# n 은 리스트 최대값의 -1 값을 가지고 있음
for i in range(0,n+1) : #바꿔지는거 검사하는 과정
    for j in range(0,n+1):
        #행끼리 바꿔서 검사하는 과정
        if i != n and board[i+1][j] != board[i][j] :
            verti_change(i,i+1,j)
            for k in range(n+1):
                max_ = max(max_,cal_board(board[n-k])) 
            max_ = max(max_,cal_board([row[j] for row in board])) 
            verti_change(i+1,i,j)
            
    for j in range(0,n):
        #열끼리 바꿔서 검사하는 과정
        if not(board[i][j+1]==board[i][j]) :
            hori_change(j,j+1,i)
            for k in range(n+1): 
                max_ = max(max_,cal_board([row[k] for row in board])) 
            max_ = max(max_,cal_board(board[i])) 
            hori_change(j+1,j,i)
print(max_)