def ambiguous_num(i) :
    if target//10<1 :
        return 1
    elif target+2//10<10 or target ==102 :
        return 2
    elif target ==99 or target==101 :
        return 1
    elif target == 100 : #초기값이 100`
        return 0    
    else :    
        return len(str(target))
import sys
input = sys.stdin.readline
b_button_list = [True] * 10 #button 0~9, +,- +누르면 +1, -누르면 -1
press_button = 0 #버튼 누르는 횟수
target = int(input().rstrip())
m = int(input().rstrip()) #M (0 ≤ M ≤ 10) number of broken button
if m == 0 : #고장난 버튼이 없는 경우
    press_button = ambiguous_num(target)
    print(press_button)
    exit()
for i in list(map(int,input().rstrip().split())) :
    b_button_list[i] = False

int_button_list = [] #True 인 숫자가 담길 list
for i in range(len(b_button_list)) :
        if b_button_list[i] :
            int_button_list.append(i)

if target == 0 or m == 10 :
    if m == 10:
        press_button = abs(target -100)
    else :
        press_button = int_button_list[0]+1
elif 98<=target<= 103 : #초기값이 100
    press_button = ambiguous_num(target)
else :
    i=j=end=want_break= 0
    t_l = len(str(target)) #타겟 넘버 자릿수
    t_l = min(t_l+1,6)
    digit = [0]*(t_l) #각자릿수 유추할 때 
    int_l = len(int_button_list)
    result = abs(target-100)
    while True :
        channel = []
        want_break = 0
        for j in range(end+1) : #넘버 생성
            channel.append(int_button_list[digit[j]])

        # 숫자 비교
        temp = int("".join(map(str,reversed(channel))))
        # print(temp)
        # print(digit)
        if temp>=target :
            result = min(temp-target+len(str(temp)),result)
        else :
            result = min(target-temp+len(str(temp)),result)
        
        for i in range(t_l) :
            if digit[i] == int_l-1 :
                want_break +=1
        if want_break == t_l and end == t_l-1 :
            break

        digit[0] +=1
        for i in range(t_l) :
            if digit[end] == int_l :
                digit[end] =0
                end+=1
                
            if digit[i] == int_l : #자릿수 올려주는 거의 최대값
                digit[i]=0
                digit[i+1] +=1  
    press_button = result            
print(press_button)