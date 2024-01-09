def solution(id_list, report, k):
    mapping = {value:index for index,value in enumerate(id_list)} #list index를 대용하기 위한 mapping용 dictionary
    bit_table = [[0 for i in range(len(id_list))] for i in range(len(id_list))] #이미 신고한 사람을 걸러내기 위한 table
    reported = {value : 0 for value in id_list} #신고 당한 횟수를 세기 위한 dicitonary
    answer = reported.copy() #신고한 사람이 정지된 횟수를 기록하기 위한 dict
    for i in range(0,len(report)) : 
        who_report = report[i].split() #input 이 "muzi frodo"식으로 muzi가 frodo를 신고한 것으로 처리해야 하니 split함수를 적용
        if bit_table[mapping[who_report[0]]][mapping[who_report[1]]] == 0 : #split한 값 muzi가 frodo  를 신고 한 적 있는지 판단
            bit_table[mapping[who_report[0]]][mapping[who_report[1]]] = 1  #muzi는 frodo를 신고했다를 기록
            reported[who_report[1]] +=1                                    #frodo에게 신고횟수 적립
       
    


    for b_index,bit in enumerate(bit_table) : #bit_table 참조 이는 id 를 가진 사람이 누굴 신고했나가 기록되어 있음
        for index,b_value in enumerate(bit) : #bit_table 
            if b_value and reported[id_list[index]] >= k : 
                answer[id_list[b_index]] +=1

    return list(answer.values())