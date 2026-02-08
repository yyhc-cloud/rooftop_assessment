def sort(numbers):
    nums = list(numbers)
    for i in range(len(nums)):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]  # perform swapping
    return nums

def getSecondLargest(numbers):
    if len(numbers) == 0:
        return None

    sorted_numbers = sort(numbers)

    # Remove duplicates
    unique_numbers = []
    for num in sorted_numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)

    if len(unique_numbers) < 2:
        return None  # not enough unique numbers

    # Second largest is second last
    return unique_numbers[-2]

def main():
    arr = [3, 1, 4, 1, 5, 9, 7]
    result = getSecondLargest(arr)
    print(result)

if __name__ == "__main__":
    main()
