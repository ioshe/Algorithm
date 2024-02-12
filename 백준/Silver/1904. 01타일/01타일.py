from sys import stdin
zero_one = [0,1,2,3,5]
target = int(stdin.readline())
for i in range(5,target+1) :
    zero_one.append((zero_one[i-1]+zero_one[i-2])%15746)
print(zero_one[target])