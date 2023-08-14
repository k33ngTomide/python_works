

def your_vat(item_price: float) -> float:
    vat = item_price * (15/100)
    return item_price + vat

def exception_checker():
    try:
        user_price = float(input("Enter the price of item:  "))
        if user_price > 0:
            print(your_vat(user_price))
        else:
            raise ValueError

    except ValueError:
        print("Invalid Input, Try again")
        exception_checker()

if __name__ == '__main__':
    exception_checker()