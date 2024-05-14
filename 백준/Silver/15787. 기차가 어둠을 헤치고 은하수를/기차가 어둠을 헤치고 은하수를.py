# https://www.acmicpc.net/problem/15787


'''
input :
5 5
1 1 1
1 1 2
1 2 2
1 2 3
3 1

output : 
2

1 command[1] command[2] : i번째 기차에(1 ≤ command[1] ≤ N) x번째 좌석에(1 ≤ command[2] ≤ MAX_TRAIN) 사람을 태워라. 이미 사람이 타있다면 , 아무런 행동을 하지 않는다.
2 command[1] command[2] : i번째 기차에 x번째 좌석에 앉은 사람은 하차한다. 만약 아무도 그자리에 앉아있지 않았다면, 아무런 행동을 하지 않는다.
3 command[1] : i번째 기차에 앉아있는 승객들이 모두 한칸씩 뒤로간다. k번째 앉은 사람은 k+1번째로 이동하여 앉는다. 만약 20번째 자리에 사람이 앉아있었다면 그 사람은 이 명령 후에 하차한다.
4 command[1] : i번째 기차에 앉아있는 승객들이 모두 한칸씩 앞으로간다. k번째 앉은 사람은 k-1 번째 자리로 이동하여 앉는다. 만약 1번째 자리에 사람이 앉아있었다면 그 사람은 이 명령 후에 하차한다.

'''

from sys import stdin
MAX_TRAIN = 20
N,M = map(int,stdin.readline().split())
commands = list(map(lambda a: list(map(int,a.split())), stdin.readlines()))

# (1 ≤ x ≤ 20)
trains = [[0 for _ in range(MAX_TRAIN)] for i in range(N)]
'''
command[0] 은 명령어
command[1] 은 기차번호
command[2] 는 부가 명령어
'''
for command in commands :
    if command[0] == 1 :
        trains[command[1]-1][command[2]-1] = 1
        continue
    if command[0] == 2 :
        trains[command[1]-1][command[2]-1] = 0
        continue
    if command[0] == 3 :
        trains[command[1]-1] = [0]+trains[command[1]-1][:MAX_TRAIN-1]
        # trains[command[1]-1][-1] = 0
        continue
    if command[0] == 4 :
        trains[command[1]-1] = trains[command[1]-1][1:] + [0]
        # trains[command[1]-1][0] = 0
        continue

count = 0
# visited = [0 for _ in range(MAX_TRAIN)]
visited = []
# print("\n".join(map(str,trains)))
# 기차 인덱스가 (1 ≤ i ≤ N) 이여서 첫번째 방을 비게 만들어서 인덱스를 맞춰줬으므로 [1:] 로 시작 

def train_check(trains) :
    global visited
    count = 0
    for train in trains :
        if train not in visited :
            visited.append(train)
            count +=1
    # for index,value in enumerate(train) :
    #     if value : 
    #         if visited[index] :
    #             return 0
    #         else :
    #             visited[index] = 1
    # return 1
    return count
count = train_check(trains)
# for train in trains[1:] :
#     count += train_check(train)
print(count)