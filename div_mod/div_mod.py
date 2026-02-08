def div_mod(x, y):
    if y == 0:
        print("Division by zero is not allowed")
        return #stop the function

    quotient = 0
    remainder = x

    while remainder >= y:
        remainder -= y
        quotient += 1

    print("Quotient:", quotient)
    print("Remainder:", remainder)


def main():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    div_mod(x, y)


if __name__ == "__main__":
    main()
