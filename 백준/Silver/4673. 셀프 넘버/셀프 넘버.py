max = 10001
bool_list = [True] * max
for i in range(1,max) :
    if bool_list[i] :
        print(i)
        k = i
        while True :
            k=k+sum(list(map(int,str(k)))) #123 => [1,2,3]
            if k>max-1:
                break
            bool_list[k] = False