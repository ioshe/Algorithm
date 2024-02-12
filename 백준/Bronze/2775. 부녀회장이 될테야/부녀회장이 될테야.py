import sys
max = 15
input = sys.stdin.readline
#num_list=[]
num_list = [[i for i in range(1,max+1)]]
for i in range(1,max):
    num_list.append([1])
    for j in range(1,max) :
        num_list[i].append(num_list[i-1][j]+num_list[i][j-1]) 

for _ in range(int(input().rstrip())) :
    n = int(input().rstrip())
    k = int(input().rstrip())
    print(num_list[n][k-1])