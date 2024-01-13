def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1) :
        # if len(s) % i : 
        #     continue
        correct = []
        for k in range(0,len(s),i) :
            correct.append(s[k:k+i])
        count = 0
        j = 0
        while j < len(s)+1 :
        #for j in range(0,len(s)+1,i) :
            temp_count = 0
            for l in range(j//i+1,len(correct)) :
                if correct[l] == s[j:j+i] :
                    temp_count +=1
                else :
                    break
            j += temp_count*i + i
            if temp_count > 0 :
                #print(f'{i}일 때 count : {temp_count}')  
                count += (temp_count*i) - len(str(temp_count+1))
                #print(f'{temp_count}{s[j:j+1]}, {(temp_count*i) -1}')
        #if count > 0 :
            #print(f'{i}일 때 count : {count}')  
        answer = min(answer,len(s) - count)
    
    return answer