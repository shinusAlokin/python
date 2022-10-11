import re

def replace_char():
    text = input("Enter a text: ")
    model_dict = {" ": "_", "_": " "}
    replaced = re.sub(r"[ _]", lambda x: model_dict[x[0]], text)
    return replaced

    
if __name__ == "__main__":
    print(replace_char())  