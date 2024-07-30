def find_minimum_button_presses(T):
    button_counts = [0, 0, 0]  # A, B, C의 누른 횟수
    times = [300, 60, 10]      # A, B, C 각각의 시간 (초)

    # 각 버튼을 최대한 많이 누르기
    for i, time in enumerate(times):
        button_counts[i] = T // time
        T %= time
    
    # T가 정확히 0이 되면 성공적으로 시간을 맞춤
    if T == 0:
        return button_counts
    else:
        return [-1]

# 입력 및 함수 호출 예제
T = int(input().strip())
result = find_minimum_button_presses(T)

# 결과 출력
if result == [-1]:
    print("-1")
else:
    print(" ".join(map(str, result)))
