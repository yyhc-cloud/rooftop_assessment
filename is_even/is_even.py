def isEven(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    
    return number % 2 == 0
    
def main():
    a = int(input("Enter the number: "))
    print(isEven(a)) 

if __name__ == "__main__":
    main()