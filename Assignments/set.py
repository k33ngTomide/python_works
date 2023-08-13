

def intersection_finder(first_list: list, second_list: list) -> list:

    intersect_list = []

    for element in first_list:
        if element in second_list:
            intersect_list.append(element)
    return intersect_list

def list_union(first_list: list, second_list: list) -> list:

    union_list = list(set(first_list))

    for element in second_list:
        if element not in union_list:
            union_list.append(element)
    return sorted(union_list)


if __name__ == '__main__':
    list_one = [20, 30, 60, 65, 75, 80, 85]
    list_two = [42, 30 , 80, 65, 68, 88, 95]

    print(list_union(list_one, list_two))
