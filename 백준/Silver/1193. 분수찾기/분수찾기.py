def find_fraction_efficient(X):
    line = 1  # 대각선의 번호
    while X > line:
        X -= line
        line += 1

    # 대각선이 홀수번째일 때와 짝수번째일 때 분자와 분모 계산
    if line % 2 == 0:
        numerator = X
        denominator = line - X + 1
    else:
        numerator = line - X + 1
        denominator = X
    
    return f"{numerator}/{denominator}"


print(find_fraction_efficient(int(input())))