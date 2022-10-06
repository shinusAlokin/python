def print_nums():
    for i in range(1, 21):
        if i % 2 == 0 or  i % 3 == 0:
            continue
        else:
            print(i)

if __name__ == "__main__":
    print_nums()