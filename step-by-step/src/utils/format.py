def key_to_4x4_matrix(key):
    letters = key.split()
    key_matrix = [[0] * 4 for _ in range(4)]
    current_letter = 0
    for i in range(4):
        for j in range(4):
            key_matrix[j][i] = letters[current_letter]
            current_letter+=1
    return key_matrix