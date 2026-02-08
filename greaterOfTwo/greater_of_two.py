def greater_of_two(number1, number2):
    return (number1 + number2 + abs(number1 - number2)) // 2 

# if x > y, then x - y > 0 → abs(x - y) = x - y
# hence x > y, then x + y + abs(x - y) // 2 will equal to (x+y+x-y)/2 = 2x/2 = x

def main():
    a = int(input("Enter first integer: "))
    b = int(input("Enter second integer: "))
    
    print("The greater number is:", greater_of_two(a, b))

if __name__ == "__main__":
    main()