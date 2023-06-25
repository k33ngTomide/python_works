pie = 4
sign = -1
user_entry = int(input('Enter the number of term: '))
print('Term\tApprx. value of pie')
for value in range(3, user_entry, 2):
    pie += 4 / value * sign
    sign *= -1

    print(f'{value}\t\t{pie}')
