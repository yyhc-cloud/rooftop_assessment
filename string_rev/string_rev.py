def rev(arr):
    if arr == "":
        return ""
    
    stack = []

    for character in arr:
        stack.append(character)

    reversed_str = ""

    while len(stack) > 0:
        reversed_str += stack.pop()

    return reversed_str

def main():
    result = rev("Hello")
    print(result)

if __name__ == "__main__":
    main()