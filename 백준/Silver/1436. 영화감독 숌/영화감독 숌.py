import sys
i=count=0
end= int(sys.stdin.readline().rstrip())
while True :
    if str(i).find('666') != -1 :
        #print(f'{count} 회차 : {i}, /6의값: {i//6}, %6의 값: {i%6}')
        count +=1
    if count == end :
        print(i)
        break
    i+=1
    