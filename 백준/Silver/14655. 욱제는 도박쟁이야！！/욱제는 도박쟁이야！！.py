int(input())
print(sum(map(lambda a : abs(int(a)),input().split())) - sum(map(lambda a : -abs(int(a)),input().split())) )