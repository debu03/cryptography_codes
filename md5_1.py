#include <iostream> 
#include <string> 
#include <bitset> 
using namespace std; 

string int_to_binary(int number) 
{ 
    // Convert integer to binary string using std::bitset 
    std::bitset<sizeof(int) * 8> bits(number); 
    return bits.to_string(); 
} 

string text_to_binary(const string &text) 
{ 
    string binary_str; 
    for (char c : text) 
    { 
        // Convert each character to its ASCII representation in binary 
        bitset<8> binary_char(c); 
        // Append binary representation to the string 
        binary_str += binary_char.to_string(); 
    } 
    return binary_str; 
} 

int main() 
{ 
    // Plaintext message 
    cout << "Enter Plain text Message" << endl; 
    string plaintext_message = "They are deterministic"; 
    // cin >> plaintext_message; 
    cout << plaintext_message << endl; 
    // "They are deterministic"; 

    // Convert plaintext message to binary 
    string binary_output = text_to_binary(plaintext_message); 

    // Print the binary representation with spaces after every 8 bits 
    cout << "\nOriginal message:" << endl; 
    for (size_t i = 0; i < binary_output.size(); ++i) 
    { 
        cout << binary_output[i]; 
        // Add space after every 8 bits 
        if ((i + 1) % 8 == 0) 
        { 
            cout << ' '; 
        } 
    } 

    int total_bits = plaintext_message.length() * 8; 

    cout << "\n\nTotal " << plaintext_message.length() << " letters including blank space -> " << plaintext_message.length() << "*8 = " << total_bits << " bits" << endl; 
    cout << "_____________________" << endl; 

    int i = 1; 
    while (512 * i < total_bits) 
    { 
        i++; 
    } 

    int padding_bits = 512 * i - 64 - total_bits; 

    cout << "\nMessage with padding bits:" << endl; 
    string padding_output = binary_output + "10000000"; 
    for (int i = 1; i <= padding_bits - 8; i++) 
    { 
        padding_output += "0"; 
    } 

    for (size_t i = 0; i < padding_output.size(); ++i) 
    { 
        cout << padding_output[i]; 
        // Add space after every 8 bits 
        if ((i + 1) % 8 == 0) 
        { 
            cout << ' '; 
        } 
    } 
    cout << "\n\nPadding bits required:" << padding_bits << endl; 
    cout << "_____________________" << endl; 

    int length_bits = 512 * i - (padding_bits + total_bits); 

    cout << "\nMessage with length bits:" << endl; 

    string Message_With_Length_Bits = padding_output; 
    for (int j = 1; j <= length_bits - 8; j++) 
    { 
        Message_With_Length_Bits += "0"; 
    } 
    Message_With_Length_Bits += int_to_binary(total_bits); 

    for (size_t i = 0; i < Message_With_Length_Bits.size(); ++i) 
    { 
        cout << Message_With_Length_Bits[i]; 
        // Add space after every 8 bits 
        if ((i + 1) % 8 == 0) 
        { 
            cout << ' '; 
        } 
    } 
    cout << "\n\nLength bits required:" << length_bits << endl; 
    return 0; 
}
