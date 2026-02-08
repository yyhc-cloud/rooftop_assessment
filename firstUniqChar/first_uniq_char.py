def first_uniq_char(arr):
    char_count_map = {}

    for character in arr:
        if character in char_count_map:
            char_count_map[character] += 1
        else: 
            char_count_map[character] = 1

    for item in arr:
        if char_count_map[item] == 1:
            return item
    
    return None

def main():
    s = "parallel"
    result = first_uniq_char(s)
    print(result)

if __name__ == "__main__":
    main()

