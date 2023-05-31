import binascii

def string_to_hex(string):
    hex_string = binascii.hexlify(string.encode()).decode()
    spaced_hex_string = ' '.join(hex_string[i:i+2] for i in range(0, len(hex_string), 2))
    return spaced_hex_string

def matrix_to_string(matrix):
    string = ''
    for row in matrix:
        for element in row:
            string += " " + element
    return string[1:]

def xor_hex_strings(hex_string1, hex_string2):
    # Convert hexadecimal strings to integers
    int1 = int(hex_string1, 16)
    int2 = int(hex_string2, 16)

    # Perform the XOR operation
    xor_result = int1 ^ int2

    # Convert the result back to a hexadecimal string
    hex_result = hex(xor_result)[2:]

    # Pad the result with leading zeros if necessary
    hex_result = hex_result.zfill(len(hex_string1))

    return hex_result

def int_matrix_to_hex_string_matrix(int_matrix):
    hex_string_matrix = []
    for row in int_matrix:
        hex_row = [hex(element)[2:].zfill(2) for element in row]
        hex_string_matrix.append(hex_row)
    return hex_string_matrix