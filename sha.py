def main():
    print("Debanjana Chanda(21BCE0019)\n")
    print("Enter original message size")
    size = int(input())
    length = 128
    print("Length field is equal to:", length)
    total_size = size + length
    print("Total message size is equal to (original message size + length field):", size, "+", length, "=", total_size)

    block_size = 1024
    b_size = block_size
    while b_size < total_size:
        b_size += block_size
    padding_bits = b_size - total_size
    print("Padding bits (total blocks bits - total Size):", b_size, "-", total_size, "=", padding_bits)
    print("Number of blocks:", b_size // block_size)

if __name__ == "__main__":
    main()
