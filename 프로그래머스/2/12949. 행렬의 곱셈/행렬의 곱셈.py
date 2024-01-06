def solution(arr1, arr2):
    row1 = len(arr1)
    col1 = len(arr1[0])
    
    row2 = len(arr2)
    col2 = len(arr2[0])
    
    answer = [[0 for i in range(col2)] for j in range(row1)]
    
    for r1 in range(row1) :
        for c2 in range(col2) :
            sum_value = 0
            for v in range(col1) :
                sum_value += arr1[r1][v]*arr2[v][c2]
            answer[r1][c2] = sum_value
    
    return answer