# https://www.acmicpc.net/problem/1408
import sys 
input = sys.stdin.readline


def size_compare(time1,time2) :
    time1_hap = time1[0] * 3600 + time1[1] * 60 + time1[2]
    time2_hap = time2[0] * 3600 + time2[1] * 60 + time2[2]
    if time1_hap < time2_hap :
        return time2_hap - time1_hap
    return 24 * 3600 - (time1_hap - time2_hap)

now_time = list(map(int,input().split(":")))
end_time = list(map(int,input().split(":")))

result = size_compare(now_time,end_time)

print(f'{result//3600:02d}:{result%3600//60:02d}:{result%60:02d}')