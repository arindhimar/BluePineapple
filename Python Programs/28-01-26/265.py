def split_list(input_list, nth):
    if nth < 0 or nth > len(input_list):
        raise ValueError("Split length must be between 0 and the length of the list")
    
    part1 = input_list[:nth]
    part2 = input_list[nth:]
    
    return part1, part2

print(split_list([1, 2, 3, 4, 5], 2))