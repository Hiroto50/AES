import copy
from src.utils.format import key_to_4x4_matrix
from src.utils.transformation import xor_hex_strings
from src.constants import SBOX

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
    preivous_key = key_to_4x4_matrix(preivous_key)
    key_matrix = key_to_4x4_matrix(round_key)
    return xor_matrices(preivous_key, key_matrix)

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

    