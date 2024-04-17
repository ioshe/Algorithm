# https://www.acmicpc.net/problem/1244

#남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.

# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 
# 그 구간에 속한 스위치의 상태를 모두 바꾼다. 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.

from sys import stdin

n = int(stdin.readline())
switches = list(map(int,stdin.readline().split()))
student_n = int(stdin.readline())
students = map(lambda a: list(map(int,a.split())), stdin.read().splitlines())

for gender,index in students :
    if gender == 1 :
        # 남학생 처리: 배수 위치 스위치 토글
        for i in range(index - 1, n, index):
            switches[i] = 1 - switches[i]
    else :
        # 여학생 처리: 최대한 넓은 대칭 구간 찾아서 토글
        left = index - 1
        right = index - 1
        while left > 0 and right < n - 1 and switches[left - 1] == switches[right + 1]:
            left -= 1
            right += 1
        # 토글 작업
        for i in range(left, right + 1):
            switches[i] = 1 - switches[i]
                                     

# 출력 형식에 맞추어 20개 단위로 줄바꿈하여 출력
for i in range(0, n, 20):
    print(" ".join(map(str, switches[i:i + 20])))
