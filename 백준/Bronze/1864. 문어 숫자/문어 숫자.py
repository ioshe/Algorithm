def octopus_numbers_to_decimal():
    # 문어 숫자와 십진수 매핑
    mapping = {
        '-': 0, '\\': 1, '(': 2, '@': 3, '?': 4,
        '>': 5, '&': 6, '%': 7, '/': -1
    }

    # 입력 받기
    while True:
        octopus_number = input()
        if octopus_number == "#":
            break
        
        decimal_value = 0
        length = len(octopus_number)
        
        # 각 기호를 대응하는 숫자로 변환 후 8진수 계산
        for i, symbol in enumerate(octopus_number):
            power = length - i - 1
            decimal_value += mapping[symbol] * (8 ** power)
        
        # 결과 출력
        print(decimal_value)

# 함수 호출
octopus_numbers_to_decimal()
