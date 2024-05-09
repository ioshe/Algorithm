# https://www.acmicpc.net/problem/2961

'''
input : 
4
1 7
2 6
3 8
4 9

output :
1
'''

def min_taste_difference(N, ingredients):
    min_diff = float('inf')  # 차이의 최소값을 초기화

    # 1부터 2^N - 1까지 모든 비트마스크 조합을 탐색 (적어도 하나의 재료를 사용해야 함)
    for mask in range(1, 1 << N):
        sour = 1
        bitter = 0
        for i in range(N):
            if mask & (1 << i):  # i번째 비트가 1인 경우, 해당 재료를 사용
                s, b = ingredients[i]
                sour *= s  # 신맛은 곱하기
                bitter += b  # 쓴맛은 더하기
        min_diff = min(min_diff, abs(sour - bitter))  # 최소 차이 업데이트

    return min_diff

# 입력 받기
N = int(input(""))
ingredients = []
for _ in range(N):
    S, B = map(int, input("").split())
    ingredients.append((S, B))

# 결과 출력
result = min_taste_difference(N, ingredients)
print(f"{result}")


