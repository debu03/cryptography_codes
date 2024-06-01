def pad_message(message):
    # Convert message to binary representation
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    
    # Calculate the length of the message in bits
    message_length = len(binary_message)
    
    # Calculate the number of padding bits required
    padding_length = (448 - (message_length + 1)) % 512
    
    # Append 1 bit followed by padding bits
    padded_message = binary_message + '1' + '0' * padding_length
    
    # Append the length of the original message in binary (64 bits)
    padded_message += format(message_length, '064b')
    
    return padded_message

def split_blocks(message, block_size):
    # Split the message into blocks of specified size
    blocks = [message[i:i+block_size] for i in range(0, len(message), block_size)]
    return blocks

# Step 1: Get user input for plaintext message
plaintext_message = input("Enter the plaintext message: ")

print("\nOriginal Message:")
print(plaintext_message)

# Step 2: Append Padding Bits
padded_message = pad_message(plaintext_message)
print("\nPadded Message after Step 1:")
print(padded_message)

# Step 3: Append Length Bits
length_bits = 64
padded_message += '0' * ((512 - (len(padded_message) + length_bits)) % 512)

# Final Output
print("\nFinal Padded Message:")
blocks = split_blocks(padded_message, 32)
for block in blocks:
    print(block)
