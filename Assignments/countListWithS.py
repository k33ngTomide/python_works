
def s_counter(data_list: list[str]):

    output = {}
    new_data_list = []
    for item in data_list:
        if item.capitalize().startswith("S"):
            new_data_list.append(item)

    for counter in range(len(new_data_list)):
        elementNumber = data_list.count(new_data_list[counter])
        output.update({new_data_list[counter]: elementNumber})

    return output

if __name__ == '__main__':
    names = ["joel", "Daniel", "Seyi", "Kelvin", "Muhammed", "Hakimi", "Segun", "Ashley", "Seyi"]

    print(s_counter(names))