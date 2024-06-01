import numpy as np

def mix_columns(state):
    mix_columns_matrix = np.array([
        [0x02, 0x03, 0x01, 0x01],
        [0x01, 0x02, 0x03, 0x01],
        [0x01, 0x01, 0x02, 0x03],
        [0x03, 0x01, 0x01, 0x02]
    ], dtype=np.uint8)

    state_array = np.array(state, dtype=np.uint8)
    result = np.zeros_like(state_array)

    for col in range(4):
        for row in range(4):
            result[row, col] = (
                gf_mul(mix_columns_matrix[row, 0], state_array[0, col]) ^
                gf_mul(mix_columns_matrix[row, 1], state_array[1, col]) ^
                gf_mul(mix_columns_matrix[row, 2], state_array[2, col]) ^
                gf_mul(mix_columns_matrix[row, 3], state_array[3, col])
            )

    return result.tolist()

def gf_mul(a, b):
    result = 0
    while a and b:
        if b & 1:
            result ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x11B
        b >>= 1
    return result

input_matrix = [
    [0x67, 0x00, 0x00, 0x00],
    [0x79, 0x00, 0x00, 0x00],
    [0x5B, 0x00, 0x00, 0x00],
    [0x3D, 0x00, 0x00, 0x00]
]
output_matrix = mix_columns(input_matrix)
print("Debanjana Chanda-21BCE0019\n")
print("Input matrix:\n")
for row in input_matrix:
    print([hex(element)[2:].upper().zfill(2) for element in row])
print("\n")
print("MixColumns Output:\n")
for row in output_matrix:
    print([hex(element)[2:].upper().zfill(2) for element in row])
