from sys import stdin

def second_list_nums(num: int):
    temp = list(map(lambda a : list(map(int,a.split())), [stdin.readline() for _ in range(num)]))
    return temp


R,C,Q = map(int,stdin.readline().split())
lights = second_list_nums(R)
views = second_list_nums(Q)

# R 이 세로
# C 가 가로
acc_sum = [[0 for i in range(C+1)] for j in range(R+1)]
acc_sum[1][1] = lights[0][0]

for i in range(2, R+1):
    acc_sum[i][1] += acc_sum[i-1][1] + lights[i-1][0]

for i in range(2, C+1):
    acc_sum[1][i] += acc_sum[1][i-1] + lights[0][i-1]

for i in range(1, R+1):
    for j in range(1, C+1):
        acc_sum[i][j] = acc_sum[i-1][j] + acc_sum[i][j-1] - acc_sum[i-1][j-1] + lights[i-1][j-1]

result = []
for r1,c1,r2,c2 in views:
    # r1,c1,r2,c2 = r1-1,c1-1,r2-1,c2-1
    temp = acc_sum[r2][c2] - acc_sum[r2][c1-1] - acc_sum[r1-1][c2] + acc_sum[r1-1][c1-1]
    result.append(temp // ((r2 - r1 + 1) * (c2 - c1 + 1)))

print("\n".join(map(str,result)))