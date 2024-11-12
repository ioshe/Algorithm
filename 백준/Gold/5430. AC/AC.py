
# https://www.acmicpc.net/problem/5430

from sys import stdin
from collections import deque
import re

T = int(stdin.readline())

for i in range(T) :
    commend = stdin.readline().strip()
    num = int(stdin.readline())
    nums = deque(re.findall(r"\d+", stdin.readline()))
    turn = 0
    
    forward = True
    end = True
    while turn < len(commend) :
        c = commend[turn]
        #  R은 배열에 있는 수의 순서를 뒤집는 함수
        if c == "R" :
            forward = forward ^ True
        elif c == "D" :
            # 배열이 비어있는데 D를 사용한 경우
            if nums :
                if forward :
                    # 첫번째 수 버리기
                    nums.popleft()
                else :
                    # 역순일 떄 
                    nums.pop()
            else :
                end = False
                break
        
        turn += 1
    
    if end :
        if forward :
            print(f'[{",".join(map(str,nums))}]')
        else :
            print(f'[{",".join(map(str,list(nums)[::-1]))}]')
    else :
        print("error")
        
        