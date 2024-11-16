def compare_operator(exp):

    answer = False

    exp_split = exp.split()

    

    num1, operator, num2 = int(exp_split[0]), exp_split[1], int(exp_split[2])

    

    if operator == "E":

        answer = -1

    elif operator == "!=":

        answer = (num1 != num2)

    elif operator == "<":

        answer = (num1 < num2)

    elif operator == ">":

        answer = (num1 > num2)

    elif operator == "<=":

        answer = (num1 <= num2)

    elif operator == ">=":

        answer = (num1 >= num2)

    elif operator == "==":

        answer = (num1 == num2)

        

    return answer

if __name__ == "__main__":

    case_num = 1

    while True:

        exp = input()

        result = compare_operator(exp)

        

        if result == -1:

            break

        else:

            print(f"Case {case_num}: {str(result).lower()}")

            case_num += 1