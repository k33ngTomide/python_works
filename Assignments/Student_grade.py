import re

number_of_students = 0
number_of_subjects = 0
default_value = "null"
student_score = []
total_score = []
def set_numbers() -> None:
    global number_of_students, number_of_subjects
    try:
        all_students = int(input("Enter the number of Students"))
        all_subjects = int(input("Enter the number of Subjects"))

        number_of_students = all_students + 1
        number_of_subjects = all_subjects + 4

    except ValueError:
        print("Invalid input. Please enter a valid number of student.")
        set_numbers()

def create_table(rows, columns, value) -> list:
    return [[value for _ in range(columns)] for _ in range(rows)]

def table_fill():
    global student_score, number_of_students, number_of_subjects, total_score

    total_score = [default_value] * number_of_students
    student_score = create_table(number_of_students, number_of_subjects, default_value)

    student_score[0][0] = "STUDENT  "

    for index in range(1, len(student_score)):
        student_score[index][0] = f"Student {index}"

    for counter in range(1, len(student_score[0])):
        student_score[0][counter] = f"SUB{counter}"

    student_score[0][len(student_score[0]) - 1] = "POSTN"
    student_score[0][len(student_score[0])- 2] = "AVEG"
    student_score[0][len(student_score[0]) - 3] = "TOTL"


def print_output():
    for row in range(1,len(student_score)):
        for column in range(len(student_score[row])):
            print (f'{student_score[row][column] : >10}', end='')
        print()

def header_output():
    for counter in range(len(student_score[0])):
        print(f'{student_score[0][counter] : >10}', end='')
    print()

def design():
    global number_of_subjects
    print('=' * (number_of_subjects*10))


def scores_filler():

    total = 0
    overall_total = 0
    total_entry= 0
    average = 0.0

    for index in range(1, len(student_score)):
        for new_index in range(1, len(student_score[index])-3):
            print(f"Entering score for {student_score[index][0]}")
            value = input(f"Entering score for Subject {new_index}")

            if re.fullmatch("^[0-9]+$", value) and 0 <= int(value) <= 100:

                score = int(value)
                student_score[index][new_index] = score
                total += score
                average = total / new_index
                new_index += 1
                overall_total += score
                total_entry += 1

            else:
                print("Invalid Score, Student score should be between 0 and 100")
                scores_filler()

            student_score[index][len(student_score[index]) - 3] = total
            total_score[0] = 0
            total_score[index] = int(total)
            student_score[index][len(student_score[index]) - 2] = f'{average: .2f}'

        total = 0
        average = 0.0

def position_calculator():
    global total_score, number_of_students

    sorted(total_score)

    for counter in range(1, len(total_score)):
        for index in range(1,len(student_score[0]) - 3):
            value = int(student_score[index][len(student_score[0])- 3])

            if total_score[counter] == value:
                student_score[index][len(student_score[0])- 1] = number_of_students - counter


if __name__ == '__main__':
    set_numbers()
    table_fill()
    scores_filler()
    position_calculator()
    design()
    header_output()
    design()
    print_output()
    design()
