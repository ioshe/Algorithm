def solution(answers):
    answer = []
    _1 = [1, 2, 3, 4, 5]
    _2 = [2, 1, 2, 3, 2, 4, 2, 5]
    _3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count_1 = count_2 = count_3 = 0
    for i,an in enumerate(answers) :
        if _1[i%5] == an :
            count_1 +=1
        if _2[i%8] == an :
            count_2 +=1
        if _3[i%10] == an :
            count_3 +=1

    ma = max(count_1, count_2, count_3)
    if count_1 ==  ma :
        answer.append(1)
    if count_2 ==  ma :
        answer.append(2)
    if count_3 ==  ma :
        answer.append(3)
    return answer