def validate_user():
    while True:
        user_name = input("Enter your User Name: ")
        password = input("Enter your Password: ")
        confirm_user = input("Enter your User Name again: ")
        confirm_pwd = input("Enter your Password again: ")

        if user_name != confirm_user or password != confirm_pwd:
            print("Invalid User Name or Password\n")
            continue
        else:
            print("You are successfully logged in!")
            break


if __name__ == "__main__":
    validate_user()
        