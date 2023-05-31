import copy
from numpy import matrix, dot
from src.utils.format import key_to_4x4_matrix
from src.utils.transformation import xor_hex_strings
from src.constants import SBOX, CONSTANT_MATRIX

def xor_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            v1 = matrix1[i][j]
            v2 = matrix2[i][j]
            row.append(xor_hex_strings(v1, v2))
        result.append(row)
    return result

def generete_round_key(preivous_key, round_key):
    return xor_matrices(preivous_key, round_key)

def sub_byte(matrix):
    s_box_result = copy.deepcopy(matrix)
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            input_byte = int(matrix[i][j], 16)
            s_box_result[i][j] = hex(SBOX[input_byte])
    return s_box_result

def shift_rows(state):
    for i in range(1, 4):
        state[i] = state[i][i:] + state[i][:i]
    return state

def mix_columns(state):
    mixed_state = []
    for i in range(len(state[0])):
        mixed_column = []
        for j in range(len(state)):
            mixed_byte = 0
            for k in range(len(state)):
                mixed_byte ^= multiply(
                    CONSTANT_MATRIX[j][k], 
                    int(state[k][i], 16))
            mixed_column.append(mixed_byte)
        mixed_state.append(mixed_column)
    return mixed_state

def multiply(a, b):
    if a == 1:
        return b
    elif a == 2:
        return multiply_by_2(b)
    elif a == 3:
        return multiply_by_3(b)
    else:
        return 0

def multiply_by_2(num):
    result = num << 1
    if result & 0x100:
        result ^= 0x1b
    return result & 0xff

def multiply_by_3(num):
    return multiply_by_2(num) ^ num


    