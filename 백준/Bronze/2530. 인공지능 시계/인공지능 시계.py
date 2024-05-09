def calculate_end_time(hours, minutes, seconds, duration):
    # 시, 분, 초를 초 단위로 전환
    total_seconds = hours * 3600 + minutes * 60 + seconds + duration

    # 총 초를 24시간 형식으로 변환
    final_hours = (total_seconds // 3600) % 24
    final_minutes = (total_seconds % 3600) // 60
    final_seconds = total_seconds % 60

    return final_hours, final_minutes, final_seconds

# 입력 받기
current_hours, current_minutes, current_seconds = map(int, input("").split())
duration_seconds = int(input(""))

# 계산된 종료 시각을 구하고 출력
end_hours, end_minutes, end_seconds = calculate_end_time(current_hours, current_minutes, current_seconds, duration_seconds)
print(end_hours, end_minutes, end_seconds)
