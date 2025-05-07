from sys import stdin

while True:
    N,M = map(int,stdin.readline().split())
    if N == 0 and M == 0:
        break
    
    nums = list(map(int,stdin.readline().split()) for i in range(N))

    ranking = {}
    for i in nums:
        for j in i:
            ranking[j] = ranking.get(j,0)+1
    
    sorted_items = sorted(ranking.items(), key=lambda a : (a[1],-a[0]), reverse=True)

    result = []
    second_value = -1 
    # print(sorted_items)
    for index,value in sorted_items[1:]:
        if value == sorted_items[0][1] :
            continue
        if result and second_value != value:
            break
        result.append(index)

        if len(result) == 1 :
            second_value = value 
    
    print(" ".join(map(str,result)))