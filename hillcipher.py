import numpy as np
from egcd import egcd

char_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
            'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
            'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

inv_char_map = {value: key for key, value in char_map.items()}

def create_key_matrix(key_str):
    key_matrix = np.zeros((2, 2), dtype=int)
    key_values = [char_map[ch] for ch in key_str.upper()]

    for i in range(2):
        for j in range(2):
            key_matrix[i][j] = key_values[i * 2 + j]

    return key_matrix

def matrix_modular_inverse(matrix, modulus):

    det = int(np.round(np.linalg.det(matrix)))
    det_inv = egcd(det, modulus)[1] % modulus 
    matrix_mod_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )

    return matrix_mod_inv

def encrypt(plain_text, key_matrix):
    plain_text = plain_text.upper()
    plain_text = plain_text.replace(" ", "")
    if len(plain_text) % len(key_matrix) != 0:
        padding_length = len(key_matrix) - (len(plain_text) % len(key_matrix))
        plain_text += 'A' * padding_length

    cipher_text = ''
    for i in range(0, len(plain_text), len(key_matrix)):
        block = plain_text[i:i + len(key_matrix)]
        block_vector = np.array([char_map[ch] for ch in block])
        encrypted_vector = np.dot(key_matrix, block_vector) % 26
        encrypted_block = ''.join([inv_char_map[num] for num in encrypted_vector])
        cipher_text += encrypted_block

    return cipher_text

def main():
    plain_text = input("Enter the plain text: ")
    key_str = input("Enter the key as a string: ")

    key_matrix = create_key_matrix(key_str)
    cipher_text = encrypt(plain_text, key_matrix)
    print("Cipher Text:", cipher_text)

    inv_key_matrix = matrix_modular_inverse(key_matrix, 26)
    print("Inverse Key Matrix:\n", inv_key_matrix)

    decrypted_message = encrypt(cipher_text, inv_key_matrix)
    print("Decrypted Text:", decrypted_message)

if __name__ == "__main__":
    main()
