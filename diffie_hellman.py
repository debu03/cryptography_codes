def power(a, b, P):
    if b == 1:
        return a
    else:
        return pow(a, b, P)

def main():
    print("DEBANJANA CHANDA ")
    P = int(input("Enter public key P: "))
    G = int(input("Enter public key G: "))

    a = int(input("Enter Alice's private key: "))
    b = int(input("Enter Bob's private key: "))

    print("\nThe value of P:", P)
    print("The value of G:", G)
    print("Alice's private key (a):", a)
    print("Bob's private key (b):", b)

    x = power(G, a, P)
    y = power(G, b, P)

    ka = power(y, a, P)
    kb = power(x, b, P)

    print("\nSecret key for Alice:", ka)
    print("Secret key for Bob:", kb)

if __name__ == "__main__":
    main()
