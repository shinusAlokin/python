def already_exists():
    roll_number = [44, 64, 69, 37, 76, 83, 95, 97]
    sample_dict = {"sojo":44, "thomas": 69, "tom":76, "jack": 11}
    roll_number = list(filter(lambda x: x in sample_dict.values(), roll_number))
    print(roll_number)
    return roll_number


if __name__ == "__main__":
    already_exists()



