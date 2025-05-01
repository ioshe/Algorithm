# https://www.acmicpc.net/problem/27964

n = input()
count = 0
for i in set(input().split()):
    if i[-6:] == "Cheese":
        count+=1

print("yummy" if count >= 4 else "sad")