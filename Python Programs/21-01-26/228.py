def count_unset_bits(input_string,start,end):
    return str(bin(int(input_string)))[2+start:end].count("0")

print(count_unset_bits("24",1,5))