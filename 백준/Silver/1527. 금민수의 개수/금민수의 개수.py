#https://www.acmicpc.net/problem/1527
MAX_LEN = 10 #1,000,000,000
KEY_VALUE = ['4','7']
result = [KEY_VALUE]
for i in range(MAX_LEN) :
    temp = []
    for j in result[i] :
        temp.append(j+"4")
        temp.append(j+"7")
    result.append(temp)

result = [int(item) for sublist in result for item in sublist]


a,b = map(int,input().split())
final=[]
for index,num in enumerate(result) :
    if a<=num<=b :
        final.append(num) 
print(len(final))