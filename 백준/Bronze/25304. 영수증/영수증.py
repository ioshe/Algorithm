total_cost, total_count = int(input()), int(input())
item_cost = 0
for i in range(total_count) :
    cost, count = map(int,input().split())
    item_cost += cost*count

if total_cost == item_cost :
    print('Yes')
else :
    print("No")