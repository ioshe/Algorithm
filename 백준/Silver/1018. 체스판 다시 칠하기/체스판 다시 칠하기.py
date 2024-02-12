from sys import stdin
n,m = map(int,stdin.readline().rstrip().split())
chess_board = []
for _ in range(n):
    chess_board.append(stdin.readline().rstrip())
w_chess_board=[[True for i in range(m)] for j in range(n)]
b_chess_board=[[True for i in range(m)] for j in range(n)]

for i in range(n):
    count = i%2
    for j in range(m):
        #w_chess_board fixing
        if count %2 == 0 :
            if chess_board[i][j] == "W":
                w_chess_board[i][j]=False
            else :
                b_chess_board[i][j]=False
        else :
            if chess_board[i][j] == "B" :
                w_chess_board[i][j]=False
            else :
                b_chess_board[i][j]=False
        count+=1
w_sum=n*m
b_sum=n*m
for i in range(n-8+1):
    for j in range(m-8+1):
        w_sum=min(w_sum,sum(sum(w[j:j+8]) for w in w_chess_board[i:i+8]))
        b_sum=min(b_sum,sum(sum(b[j:j+8]) for b in b_chess_board[i:i+8]))

print(min(w_sum,b_sum))