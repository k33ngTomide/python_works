
def calculator() -> str:
    number_1, operator, number_2 = input('').split(" ", 2)

    if operator == "+":
        answer_addition = number_1 + number_2
        return str(answer_addition)

    elif operator == "-":
        answer_subtract = number_1 - number_2
        return str(answer_subtract)

    elif operator == "*":
        answer_multiply = number_1 * number_2
        return str(answer_multiply)

    invalid = "Invalid Operator"
    return invalid


def calca():
    print("Welcome to a Simple Calculator")
    print(calculator())


calca()
