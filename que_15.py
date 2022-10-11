import re 

def validate_phone_number():
    number = "9198978673234"
    pattern = re.compile("\+?(0|91)?[6-9][0-9]{9}")
    is_valid = lambda x: pattern.match(x)
    if is_valid(number):
        print("Valid phone number")
    else:
        print("Number is invalid")

if __name__ == "__main__":
    print(validate_phone_number())   