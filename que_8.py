
def most_common():
    text = input("Enter text to count: ")
    word_dict = {}
    for word in text.split():
        if word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    word_dict = dict(list(sorted(word_dict.items(), key=lambda item: item[1], reverse=True))[:3])
    print(word_dict)
    return word_dict

if __name__ == "__main__":
    most_common()