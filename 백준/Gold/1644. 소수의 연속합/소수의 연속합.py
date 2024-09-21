# https://www.acmicpc.net/problem/1644

N = int(input())


## 에라토스테네스의 체를 이용해 소수만 걸러낸다.
sosu = [False for i in range(N + 1)]
sosu_list = []
for i in range(2,N+1) :
    if not(sosu[i]) :
       sosu[i] = True
       sosu_list.append(i)
       for j in range(i,N+1,i) :
           sosu[j] = True

if N == 1 :
    print(0)
elif N <= 3 :
    print(1)
else :
    ## 투포인터를 이용해 수를 찾는다.
    left = 0
    right = 1
    count = 0
    hap = sosu_list[0] + sosu_list[1]
    # 조건을 어케 하지
    while left < right:
        if hap == N : 
            count +=1 
            right +=1
            hap += sosu_list[right]
        elif hap < N :
            right+=1
            hap+=sosu_list[right]
        else :
            hap -= sosu_list[left]
            left +=1 
        
    if sosu_list[-1] == N :
        count += 1
    print(count)