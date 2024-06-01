#include <iostream>
#include <cstdint>
using namespace std;

const uint32_t INIT_A = 0x67452301;
const uint32_t INIT_B = 0xEFCDAB89;
const uint32_t INIT_C = 0x98BADCFE;
const uint32_t INIT_D = 0x10325476;

#define F(X, Y, Z) (((X) & (Y)) | ((~X) & (Z)))
#define G(X, Y, Z) (((X) & (Z)) | ((Y) & (~Z)))
#define H(X, Y, Z) ((X) ^ (Y) ^ (Z))
#define I(X, Y, Z) ((Y) ^ ((X) | (~Z)))

const uint32_t K[] = {
    0x00000000, 0xd76aa478, 0xe8c7b756, 0x242070db,
};

inline uint32_t LEFT_ROTATE(uint32_t x, uint32_t c)
{
    return (x << c) | (x >> (32 - c));
}

void round1(uint32_t &a, uint32_t b, uint32_t c, uint32_t d, uint32_t x,
            uint32_t s, uint32_t ac)
{
    a = LEFT_ROTATE(a + F(b, c, d) + x + ac, s) + b;
}

void round2(uint32_t &a, uint32_t b, uint32_t c, uint32_t d, uint32_t x,
            uint32_t s, uint32_t ac)
{
    a = LEFT_ROTATE(a + G(b, c, d) + x + ac, s) + b;
}

void md5(uint32_t &a, uint32_t &b, uint32_t &c, uint32_t &d, const uint32_t *x)
{
    round1(a, b, c, d, x[0], 7, 0xd76aa478);
    round2(d, a, b, c, x[1], 12, 0xe8c7b756); // Round 2
}

int main()
{
    cout << "Debanjana Chanda (21BCE0019)\n"
         << endl;

    uint32_t a = INIT_A;
    uint32_t b = INIT_B;
    uint32_t c = INIT_C;
    uint32_t d = INIT_D;

    // Given inputs
    uint32_t A = 0x76543210; // Update A
    uint32_t B = 0x7330c604; // Update B
    uint32_t C = 0x89abcdef; // Update C
    uint32_t D = 0xfedcba98; // Update D

    uint32_t message_block[2] = {A, B}; // Update message_block

    md5(a, b, c, d, message_block);

    std::cout << "Round 1 MD5 Buffer A: " << std::hex << a << std::endl;
    std::cout << "Round 1 MD5 Buffer B: " << std::hex << b << std::endl;
    std::cout << "Round 1 MD5 Buffer C: " << std::hex << c << std::endl;
    std::cout << "Round 1 MD5 Buffer D: " << std::hex << d << std::endl;

    // Reset the values for round 2
    a = INIT_A;
    b = INIT_B;
    c = INIT_C;
    d = INIT_D;

    // Update message_block for round 2
    message_block[0] = c; // Update with the result of round 1
    message_block[1] = d; // Update with the result of round 1

    md5(a, b, c, d, message_block);

    std::cout << "\nRound 2 MD5 Buffer A: " << std::hex << a << std::endl;
    std::cout << "Round 2 MD5 Buffer B: " << std::hex << b << std::endl;
    std::cout << "Round 2 MD5 Buffer C: " << std::hex << c << std::endl;
    std::cout << "Round 2 MD5 Buffer D: " << std::hex << d << std::endl;

    return 0;
}
