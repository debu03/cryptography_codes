def hex_to_binary(hex_string):
    binary_string = bin(int(hex_string, 16))[2:]
    binary_string = binary_string.zfill(64)
    return binary_string
def initial_permutation_with_positions(binary_string, permutation_table):
    permuted_string = ''.join(binary_string[i - 1] for i in permutation_table)
    return permuted_string
def final_permutation_with_positions(binary_string, permutation_table):
    permuted_string = ''.join(binary_string[i - 1] for i in permutation_table)
    return permuted_string

print("Enter the hexadecimal input: 0002000000000001 ")
hex_input = str(input())
initial_permutation_table = [
58, 50, 42, 34, 26, 18, 10, 2,
60, 52, 44, 36, 28, 20, 12, 4,
62, 54, 46, 38, 30, 22, 14, 6,
64, 56, 48, 40, 32, 24, 16, 8,
57, 49, 41, 33, 25, 17, 9, 1,
59, 51, 43, 35, 27, 19, 11, 3,
61, 53, 45, 37, 29, 21, 13, 5,
63, 55, 47, 39, 31, 23, 15, 7
]
final_permutation_table = [
40, 8, 48, 16, 56, 24, 64, 32,
39, 7, 47, 15, 55, 23, 63, 31,
38, 6, 46, 14, 54, 22, 62, 30,
37, 5, 45, 13, 53, 21, 61, 29,
36, 4, 44, 12, 52, 20, 60, 28,
35, 3, 43, 11, 51, 19, 59, 27,
34, 2, 42, 10, 50, 18, 58, 26,
33, 1, 41, 9, 49, 17, 57, 25
]
binary_input = hex_to_binary(hex_input)
# Initial Permutation
output_permuted_initial = initial_permutation_with_positions(binary_input,
initial_permutation_table)
# Final Permutation
output_permuted_final = final_permutation_with_positions(output_permuted_initial,
final_permutation_table) 
hex_output_initial = hex(int(output_permuted_initial, 2))[2:].zfill(16)
hex_output_final = hex(int(output_permuted_final, 2))[2:].zfill(16)
print("Debanjana Chanda:21BCE0019")
print("Input (64-bit Hexadecimal):", hex_input)
print("Binary Representation:", binary_input)
print("Output after Initial Permutation:", hex_output_initial.upper())
print("Output after Final Permutation:", hex_output_final.upper())