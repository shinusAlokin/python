import re

def get_email():
    text = input("Enter your email: ")
    email = re.findall(r"[a-zA-Z0-9\.\-\_]+@", str(text))
    return email

if __name__ == "__main__":
    print(get_email())
