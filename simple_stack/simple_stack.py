# Push an item onto the stack
def push(item, arr):
    arr.append(item)

# Pop the top item from the stack
def pop(arr):
    if len(arr) == 0:
        return None
    return arr.pop() #use pop from list

# Peek at the top item without removing
def peek(arr):
    if len(arr) == 0:
        return None
    return arr[-1]

def main():
    stack = []

    push(10, stack)
    push(20, stack)
    push(30, stack)

    print("Stack:", stack)
    print("Top element:", peek(stack))

    popped = pop(stack)
    print("Popped:", popped)
    print("Stack after pop:", stack)

if __name__ == "__main__":
    main()


