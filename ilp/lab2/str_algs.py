def invert_str(input_str):
    str = ''
    for i in range(len(input_str)-1, -1, -1):
        str += input_str[i]
    return  str



print(invert_str("chto"))