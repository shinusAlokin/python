def count_upp_low():
    text = input("Enter a string: ")
    upper = 0
    lower = 0
    for i in str(text):
        if i.isupper():
            upper += 1
        else:
            lower += 1
    print(f"Number of Upper case is: {upper}\n Number of Lowercase is: {lower}")


print(count_upp_low())