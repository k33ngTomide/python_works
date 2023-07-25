
def unique(data_list: list) -> list:

    new_list = []
    for item in data_list:
        if item in new_list:
            continue
        else:
            new_list+=[item]

    return new_list

if __name__ == '__main__':
    print(unique([34,23,24,21,32,43,23,44,54,34,23,22,76,77,33,24,34]))