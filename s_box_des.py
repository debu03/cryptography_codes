def s_box(input_bits, s_box_number):
    s_boxes = {
    7: [
        [4, 11, 2, 14, 15, 00, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 15, 0, 15, 14, 2, 3, 12]
        ],
    2: [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
        ],
    }
    if len(input_bits) != 6 or not all(bit in '01' for bit in input_bits):
        raise ValueError("Input must be a 6-bit binary string")
    row = int(input_bits[0] + input_bits[5], 2)
    col = int(input_bits[1:5], 2)
    output_decimal = s_boxes[s_box_number][row][col]
    output_bits = format(output_decimal, '04b')
    return output_bits
print("Debanjana Chanda:21BCE0019\n")
inputbox_7 = str(input("Enter the S Box 7 input 6 bit binary string:\n"))
outputbox_7 = s_box(inputbox_7, 7)
inputbox_2 = str(input("Enter the S Box 2 input 6 bit binary string:\n"))
outputbox_2 = s_box(inputbox_2, 2)
print("S-Box 7:")
print(f"Input: {inputbox_7}")
print(f"Output: {outputbox_7}\n")
print("S-Box 2:")
print(f"Input: {inputbox_2}")
print(f"Output: {outputbox_2}\n")