def find_words_starting_with_a_or_e(input_string):
    words = input_string.split()
    result = [word for word in words if word.lower().startswith(('a', 'e'))]
    return result

