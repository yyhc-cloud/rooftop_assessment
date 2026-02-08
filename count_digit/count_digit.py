def count_digit(target, number):
    result = 0
    for digit in str(number):       # convert number to string to iterate
        if int(digit) == target:    # compare the item in integer form with the target 3
            result += 1
    return result

def main():
    n = 332
    print("Number of 3s:", count_digit(3, n))

if __name__ == "__main__":
    main()
