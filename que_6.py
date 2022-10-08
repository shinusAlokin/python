
def divisible_five():
    num_list = [43, 65, 52, 70, 85, 25]
    nums = list(filter(lambda x: x%5==0, num_list))
    nums.sort()
    print(nums)
    return nums


if __name__ == "__main__":
    divisible_five()