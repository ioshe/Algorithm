count = int(input())
item_list = list(map(int,input().split()))
choice = int(input())
total_count = 0
for character in item_list :
    if character == choice :
        total_count +=1
print(total_count)