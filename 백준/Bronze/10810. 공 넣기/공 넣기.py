volume,trial = map(int,input().split())
num_list = [ 0 for i in range(volume)] #0을 한줄로 채우는 법
for i in range(trial) :
    i,j,k = map(int, input().split())
    for repeat in range(i-1,j) :
        num_list[repeat] = k
print(*num_list)
