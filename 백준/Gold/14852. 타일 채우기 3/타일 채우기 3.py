n=int(input())
num_list=[1,2,7]
multi_list = [0,0,0]
if n>2 :
    for i in range(3,n+1):
        multi_list.append((num_list[i-3]*2+multi_list[i-1])%1000000007)
        num_list.append((num_list[i-2]*3+num_list[i-1]*2+multi_list[i])%1000000007)
print(num_list[n]%1000000007)