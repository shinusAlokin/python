
def sum_odd_even():
    even = 0
    odd = 0
    for i in range(15, 36):
        if i % 2 == 0:
            even += i
        else:
            odd += i
    print(f"Sum of odd is: {odd}")
    print(f"Sum of even is: {even}")
    return (odd, even)

if __name__ == "__main__":
    sum_odd_even()