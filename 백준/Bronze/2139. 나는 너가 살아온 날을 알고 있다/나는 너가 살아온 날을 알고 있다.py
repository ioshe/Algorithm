def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def day_of_year(day, month, year):
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_months[1] = 29  # 2월의 일수를 29일로 변경
    
    # 1월 1일부터 주어진 날짜까지의 일수 합산
    return sum(days_in_months[:month-1]) + day

# 입력을 받고 처리하는 부분
import sys
input = sys.stdin.read
data = input().splitlines()

for line in data:
    if line == "0 0 0":
        break
    day, month, year = map(int, line.split())
    print(day_of_year(day, month, year))
