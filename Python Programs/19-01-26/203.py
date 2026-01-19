def find_humming_distance(number1, number2):
    return bin(number1 ^ number2).count("1")


number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
print(find_humming_distance(number1, number2))

    