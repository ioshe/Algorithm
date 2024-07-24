# 입력값을 받습니다.

K, N, M = map(int, input().split())

# 필요한 총 금액을 계산합니다.

total_cost = K * N

# 부모님께 받아야 하는 금액을 계산합니다.

needed_money = total_cost - M

# 만약 모자란 금액이 음수일 경우 0으로 처리합니다.

if needed_money < 0:

    needed_money = 0

# 결과를 출력합니다.

print(needed_money)

