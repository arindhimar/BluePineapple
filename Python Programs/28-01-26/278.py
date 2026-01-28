def count_elements_before_record(input_tuple, record):
    if record not in input_tuple:
        raise ValueError("Record not found in the tuple")
    
    count = 0
    for element in input_tuple:
        if element == record:
            break
        count += 1
    
    return count

try:
    print(count_elements_before_record((10, 20, 30, 40, 50), 30))
except ValueError as e:
    print(e)