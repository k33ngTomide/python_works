
def getSumOfListWithFor(numbers: list) -> int:
    total = 0
    for number in numbers:
        total += number

    return total

def  getSumOfListWithWhile(numbers: list) -> int:
    total = 0
    counter = 0

    while counter < numbers.length :
        total += numbers[counter]
    counter+=1

    return total

