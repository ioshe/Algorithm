
def solution(expression):
    operators = ['+-*', '+*-', '-+*', '-*+', '*+-', '*-+']
    result = 0
    for op in operators :
        split_string = expression.split(op[0])
        new_string = f')){op[0]}(('.join(split_string)
        split_string = new_string.split(op[1])
        new_string = f'){op[1]}('.join(split_string)
        temp = eval(f'(({new_string}))')
        if result < abs(temp) :
            result = abs(temp)
        
    return result