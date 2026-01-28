def split_list(input_list, split_length):
    if split_length < 0 or split_length > len(input_list):
        raise ValueError("Split length must be between 0 and the length of the list")
    
    part1 = input_list[:split_length]
    part2 = input_list[split_length:]
    
    return part1, part2

print(split_list([1, 2, 3, 4, 5], 2))