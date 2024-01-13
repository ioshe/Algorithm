def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1) :
        correct = [s[k:k+i] for k in range(0,len(s),i)]
        count = j = 0
        while j < len(s)+1 :
            temp_count = 0
            for l in range(j//i+1,len(correct)) :
                if correct[l] == s[j:j+i] :
                    temp_count +=1
                else :
                    break
            j += temp_count*i + i
            if temp_count > 0 :
                count += (temp_count*i) - len(str(temp_count+1)) 
        answer = min(answer,len(s) - count)
    return answer