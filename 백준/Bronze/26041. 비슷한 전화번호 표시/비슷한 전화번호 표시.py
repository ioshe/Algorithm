A = list(input().split())
B = input()
cnt = 0

for i in range(len(A)) :
    if A[i] == B :	# 같으면
        continue	# continue
    else :	# 다르면
        if A[i][:len(B)] == B :	# 접두사를 가질 경우에
            cnt += 1	# cnt + 1
print(cnt)