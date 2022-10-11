def count_vowels():
    vowels = list('aeiou')
    text = input("Enter your text: ")
    count = 0
    for i in text: 
        if i in vowels:
            count += 1
    return count


if __name__ == "__main__":
    print(count_vowels())