def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def mod_inverse(e, phi_n):
    x = 1
    while True:
        if (x * e) % 160 == 1:
            return x
        x += 1

def modular_pow(base, exponent, modulus):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    return result

if __name__ == "__main__":
    print("Debanjana Chanda-21BCE0019")
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter another prime number (q): "))
    M = int(input("Enter an integer (M): "))

    if not is_prime(p) or not is_prime(q):
        print("Both inputs must be prime numbers.")
        exit(1)

    n = p * q
    print("n:", n)
    phi_n = (p - 1) * (q - 1)
    print("phi(n):", phi_n)

    e = 2
    while gcd(e, phi_n) != 1:
        e += 1
    print("e:", e)

    d = mod_inverse(e, phi_n)
    print("d:", d)

    C = modular_pow(M, e, n)
    print("Encrypting...")
    print("Ciphertext (C):", C)

    print("Decrypting...")
    M1 = modular_pow(C, d, n)
    print("Decrypted value (M1):", M1)
