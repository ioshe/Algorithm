while True:

    # 세 변의 길이를 입력받음

    a, b, c = map(int, input().split())

    # 종료 조건 (0 0 0 입력 시)

    if a == 0 and b == 0 and c == 0:

        break

    # 삼각형의 유효성 검사

    # 가장 긴 변을 찾음

    longest = max(a, b, c)

    # 가장 긴 변이 나머지 두 변의 합보다 작거나 같은지 확인

    if longest >= (a + b + c - longest):

        print("Invalid")

    else:

        # 삼각형의 유형 결정

        if a == b == c:

            print("Equilateral")

        elif a == b or b == c or a == c:

            print("Isosceles")

        else:

            print("Scalene")

