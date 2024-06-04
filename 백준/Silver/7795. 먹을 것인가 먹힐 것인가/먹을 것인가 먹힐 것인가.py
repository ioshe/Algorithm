# https://www.acmicpc.net/problem/7795

from sys import stdin

T = int(stdin.readline())
result = []
for _ in range(T) :
    N,M = map(int,stdin.readline().split())
    count = 0
    n_nums = list(map(int,stdin.readline().split()))
    m_nums = list(map(int,stdin.readline().split()))

    n_nums.sort(reverse=True)
    m_nums.sort(reverse=True)

    m_count = len(m_nums)
    j = 0
    i = 0
    while i < N and j < M :
        if j < M and n_nums[i] > m_nums[j] :
            count += m_count
            i+=1
        elif n_nums[i] <= m_nums[j] :
            m_count -= 1
            j+=1
        #print(f'{n_nums[i]}에서 count = {count} m_count = {m_count} ')

    result.append(count)

print("\n".join(map(str,result)))
