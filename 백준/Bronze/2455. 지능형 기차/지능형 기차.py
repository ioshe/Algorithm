import sys

def max_people_on_train():
    people_on_train = 0
    max_people = 0

    # 4개의 역에 대해 입력을 받음
    for _ in range(4):
        # 한 줄을 읽어서 공백을 기준으로 분리한 후, 정수로 변환
        off, on = map(int, sys.stdin.readline().split())
        
        # 사람이 내리고
        people_on_train -= off
        # 사람이 탐
        people_on_train += on
        
        # 최대 인원 수를 업데이트
        max_people = max(max_people, people_on_train)

    return max_people

# 결과 출력
print(max_people_on_train())
