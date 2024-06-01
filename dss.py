import random

def mod_exp(base, exp, modulus):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exp //= 2
    return result

def generate_key(p, q, h):
    r = mod_exp(h, (p - 1) // q, p)
    x = random.randint(1, q - 1)
    y = mod_exp(r, x, p)
    return x, y

def sign_message(p, q, r, x, w, k):
    while True:
        k = random.randint(1, q - 1)
        if k > 0 and k < q:
            break
    s1 = mod_exp(r, k, p) % q
    s2 = (w * s1 + x * k) % q
    return s1, s2

def verify_signature(p, q, r, y, w, s1, s2):
    v = mod_exp(r, w, p)
    s1_inv = pow(s1, -1, q)
    u1 = (s2 * s1_inv) % q
    u2 = (-w * s1_inv) % q
    v1 = (mod_exp(r, u1, p) * mod_exp(y, u2, p)) % p % q
    return v1 == s1

def main():
    print("Soumil Aggarwal (21BCE0252)")
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))
    h = int(input("Enter h: "))
    x = int(input("Enter private key x: "))
    w = int(input("Enter w: "))
    k = int(input("Enter k: "))

    r = mod_exp(h, (p - 1) // q, p)
    y = mod_exp(r, x, p)

    print("Public key (p, q, r, y): ", (p, q, r, y))

    s1, s2 = sign_message(p, q, r, x, w, k)
    print("Generated signature (s1, s2): ", (s1, s2))

    verification = verify_signature(p, q, r, y, w, s1, s2)
    if verification:
        print("Signature is verified. Message integrity ensured.")
    else:
        print("Verification failed. Message may have been tampered with.")

if __name__ == "__main__":
    main()
