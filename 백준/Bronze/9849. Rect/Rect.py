def find_intersection_area(rectangles):
    # 처음 직사각형의 범위
    x1_intersection, x2_intersection = rectangles[0][0], rectangles[0][1]
    y1_intersection, y2_intersection = rectangles[0][2], rectangles[0][3]
    
    # 나머지 직사각형들에 대해 교차 범위 찾기
    for x1, x2, y1, y2 in rectangles[1:]:
        x1_intersection = max(x1_intersection, x1)
        x2_intersection = min(x2_intersection, x2)
        y1_intersection = max(y1_intersection, y1)
        y2_intersection = min(y2_intersection, y2)
        
        # 교차 영역이 없으면 넓이는 0
        if x1_intersection >= x2_intersection or y1_intersection >= y2_intersection:
            return 0
    
    # 교차된 영역이 있으면 넓이 계산
    return (x2_intersection - x1_intersection) * (y2_intersection - y1_intersection)

# 입력 받기
n = int(input())
rectangles = [tuple(map(int, input().split())) for _ in range(n)]

# 교차 영역의 넓이 출력
print(find_intersection_area(rectangles))
