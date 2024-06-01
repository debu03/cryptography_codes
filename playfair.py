class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col


def generate_matrix(key):
    mat = [[' ']*5 for _ in range(5)]
    flag = [0]*26
    x, y = 0, 0

    for i in range(len(key)):
        if key[i] == 'j':
            key = key[:i] + 'i' + key[i+1:]

        if flag[ord(key[i]) - ord('a')] == 0:
            mat[x][y] = key[i]
            flag[ord(key[i]) - ord('a')] = 1
            y += 1

        if y == 5:
            x += 1
            y = 0

    for ch in range(ord('a'), ord('z')+1):
        if ch == ord('j'):
            continue

        if flag[ch - ord('a')] == 0:
            mat[x][y] = chr(ch)
            flag[ch - ord('a')] = 1
            y += 1

        if y == 5:
            x += 1
            y = 0

    return mat


def format_message(msg):
    for i in range(len(msg)):
        if msg[i] == 'j':
            msg = msg[:i] + 'i' + msg[i+1:]

    for i in range(1, len(msg), 2):
        if msg[i-1] == msg[i]:
            msg = msg[:i] + 'x' + msg[i:]

    if len(msg) % 2 != 0:
        msg += 'x'

    return msg


def get_position(mat, c):
    for i in range(5):
        for j in range(5):
            if c == mat[i][j]:
                return Position(i, j)


def encrypt(message, mat):
    ctext = ""
    for i in range(0, len(message), 2):
        p1 = get_position(mat, message[i])
        p2 = get_position(mat, message[i + 1])
        x1, y1 = p1.row, p1.col
        x2, y2 = p2.row, p2.col

        if x1 == x2:
            ctext += mat[x1][(y1 + 1) % 5] + mat[x2][(y2 + 1) % 5]
        elif y1 == y2:
            ctext += mat[(x1 + 1) % 5][y1] + mat[(x2 + 1) % 5][y2]
        else:
            ctext += mat[x1][y2] + mat[x2][y1]

    return ctext


def decrypt(message, mat):
    ptext = ""
    for i in range(0, len(message), 2):
        p1 = get_position(mat, message[i])
        p2 = get_position(mat, message[i + 1])
        x1, y1 = p1.row, p1.col
        x2, y2 = p2.row, p2.col

        if x1 == x2:
            ptext += mat[x1][(y1 - 1) % 5] + mat[x2][(y2 - 1) % 5]
        elif y1 == y2:
            ptext += mat[(x1 - 1) % 5][y1] + mat[(x2 - 1) % 5][y2]
        else:
            ptext += mat[x1][y2] + mat[x2][y1]

    return ptext


def print_matrix(mat):
    for k in range(5):
        for j in range(5):
            print(mat[k][j], end='  ')
        print()


if __name__ == "__main__":
    print("Debanjana Chanda:21BCE0019")
    print("Enter plaintext: ", end="")
    plaintext = input()
    print("Enter key: ", end="")
    key = input()
    mat = generate_matrix(key)

    print("Key Matrix:")
    print_matrix(mat)

    print("Actual Message:", plaintext)

    fmsg = format_message(plaintext)
    print("Formatted Message:", fmsg)

    ciphertext = encrypt(fmsg, mat)
    print("Encrypted Message:", ciphertext)

    decryptmsg = decrypt(ciphertext, mat)
    print("Decrypted Message:", decryptmsg)
