def odd_index():
    num_list = [1, 2, 3, 4, 5, 6, 7, "a"]
    odd_list = []
    for i, j in enumerate(num_list):
        if i%2 != 0:
            odd_list.append(j)
        else:
            continue
    print(odd_list)
    return odd_list


if __name__ == "__main__":
    odd_index()
