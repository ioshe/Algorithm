def generate_sequence(n):
    # 수열 생성 함수
    sequence = []
    for i in range(1, n + 1):
        sequence.extend([i] * i)
    return sequence

def sum_of_subsequence(sequence, a, b):
    # 부분 수열의 합을 계산하는 함수
    return sum(sequence[a-1:b])

# 입력
a, b = map(int, input().split())

# 수열 생성 (A, B의 최대값이 1000이므로 충분히 큰 수까지 계산)
sequence = generate_sequence(45)  # 45까지 하면 1035번째 위치까지 계산 가능

# 결과 출력
result = sum_of_subsequence(sequence, a, b)
print(result)
