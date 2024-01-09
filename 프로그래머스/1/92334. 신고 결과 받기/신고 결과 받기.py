# if 
# 비트마스킹을 한다. bit_list = [[0 for i in range(len(id_list))] for i in range(len(id_list))] 
# 비트 마스킹을 통해 접근 방법은 report[i].split() 한 값으로 i,j 참조를 할텐데 매핑을 어떤식으로 시켜줘야 할려나 
# 1딕셔너리로 매핑을?
# 2. 리스트 index로 
def solution(id_list, report, k):
    mapping = {value:index for index,value in enumerate(id_list)} #list index를 대용하기 위한 mapping용 dictionary
    bit_table = [[0 for i in range(len(id_list))] for i in range(len(id_list))] #이미 신고한 사람을 걸러내기 위한 table
    reported = {value : 0 for value in id_list} #신고 당한 횟수를 세기 위한 dicitonary
    answer = reported.copy() #신고한 사람이 정지된 횟수를 기록하기 위한 dict
    for i in range(0,len(report)) : 
        who_report = report[i].split() #input 이 "muzi frodo"식으로 muzi가 frodo를 신고한 것으로 처리해야 하니 split함수를 적용
        if bit_table[mapping[who_report[0]]][mapping[who_report[1]]] == 0 :
            bit_table[mapping[who_report[0]]][mapping[who_report[1]]] = 1
            reported[who_report[1]] +=1
       
    


    for b_index,bit in enumerate(bit_table) :
        for index,b_value in enumerate(bit) :
            if b_value and reported[id_list[index]] and reported[id_list[index]] >= k :
                answer[id_list[b_index]] +=1

    return list(answer.values())