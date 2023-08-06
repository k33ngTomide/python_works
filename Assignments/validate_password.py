import re
import time

password = ""
def password_validator():
    global password
    password = input("Enter a password: ")
    length_check()

def length_check():
    global password
    if len(password) >= 8:
        uppercase_check()
    else:
        print("Invalid\nPassword must be longer than 8 characters")
        password_validator()
def uppercase_check():
    global password
    if re.search(".*?[A-Z]", password):
        lowercase_check()
    else:
        print("Invalid\npassword must contain at least one uppercase letter")
        password_validator()

def lowercase_check():
    global password
    if re.search(".*?[a-z]", password):
        number_check()
    else:
        print("Invalid\npassword must contain at least one lowercase letter")
        password_validator()
def number_check():
    global password
    if re.search(".*?[0-9]", password):
        special_char_check()
    else:
        print("Invalid\npassword must contain at least one number")
        password_validator()

def special_char_check():
    global password
    if re.search(".*?[!@$%^#&*_><]", password):
        saved()
    else:
        print("Invalid\npassword must contain at least one special character")
        password_validator()

def saved():
    global password
    print("Password is Valid")
    print("Saving", end="")
    for _ in range(10):
        print(">", end="")
        time.sleep(0.5)
    print(f"\n\nPassword saved Successful\nPassword is saved as {password}")

if __name__ == '__main__':
    password_validator()