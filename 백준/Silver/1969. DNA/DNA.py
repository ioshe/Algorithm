from sys import stdin

N,M = map(int,stdin.readline().split())
texts = list(map(lambda a : a.strip(),stdin.readlines()))
result = []
count = 0
for i in range(M):
    alpha = [0 for i in range(26)]
    for j in range(N): 
        alpha[ord(texts[j][i])-65] +=1
    
    max_alpha,alpha_index = 0,0
    for index,value in enumerate(alpha):
        if max_alpha < value:
            max_alpha = value
            alpha_index = index
    
    result.append(chr(65 + alpha_index))
    count += N - max_alpha

print("".join(result))
print(count)