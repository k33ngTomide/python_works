from threading import Event


def main() -> None:
    first_number, operator, second_number = input("Enter:  ").split(" ", 2)

    first_number = int(first_number)
    second_number = int(second_number)
    print("Please wait.\nLoading", end= " ")
    waiting()

    if operator == "+":
        answer = first_number + second_number
        print("""Operator found. Processing operation
                please wait""", end=" ")
        waiting()
        print("\n",first_number, " + ", second_number, " = ", answer)
    elif operator == "-":
        answer = first_number - second_number
        print("""Operator found. Processing operation
                    please wait""", end=" ")
        waiting()
        print("\n", first_number, " - ", second_number, " = ", answer)
    elif operator == "*":
        answer = first_number * second_number
        print("""Operator found. Processing operation
                        please wait""", end=" ")
        waiting()
        print("\n", first_number, " * ", second_number, " = ", answer)
    else:
        print("""The operation you entered is under processing. 
                please wait. Reloading""", end=" ")
        waiting()
        print("\nOperator Not found, please try again later")


def waiting() -> None:
    for load in range(1, 6):
        print(">", end=" ")
        Event().wait(1.0)
    print()

if __name__ == '__main__':
    main()