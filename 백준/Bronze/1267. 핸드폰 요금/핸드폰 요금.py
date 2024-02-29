from sys import stdin

n = int(stdin.readline())

nums = list(map(int, stdin.readline().split()))

y = m = 0  # 변수 y를 영식 요금제, m을 민식 요금제로 사용

for i in nums:

    y += ((i // 30)+1) * 10  # 영식 요금제 계산

    m += ((i // 60)+1) * 15  # 민식 요금제 계산

    

if y == m:

    print(f'Y M {y}')  # y와 m의 값이 같으므로 어느 변수를 출력해도 상관없음

elif m < y:

    print(f'M {m}')

else:

    print(f'Y {y}')

