def replace_last_element_with_list(original_list, new_list):
    if not original_list:
        return new_list
    return original_list[:-1] + new_list

