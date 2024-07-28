def convert_base(N, B):
    # 결과를 저장할 문자열
    result = []
    
    # N이 0이 아닐 때까지 반복
    while N > 0:
        remainder = N % B
        # 10 이상의 숫자를 알파벳으로 변환
        if remainder >= 10:
            result.append(chr(remainder - 10 + ord('A')))
        else:
            result.append(str(remainder))
        N //= B  # N을 B로 나눈 몫으로 갱신
    
    # 결과 리스트를 뒤집어서 문자열로 결합
    if not result:  # N이 0인 경우 빈 리스트 방지
        return '0'
    return ''.join(reversed(result))

# 입력 받기
N, B = map(int, input().split())

# 결과 출력
print(convert_base(N, B))
