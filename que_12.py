from itertools import permutations

def find_anagram():
    text = input("Enter a word to find anagram: ")
    comb = permutations(str(text), len(text))
    ls = ["".join(i) for i in comb][1:]
    return ls

if __name__ == "__main__":
    print(find_anagram())