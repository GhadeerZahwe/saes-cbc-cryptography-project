# S-AES CBC Cryptographic System (Educational Implementation)

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Status](https://img.shields.io/badge/Project-Completed-success)
![Purpose](https://img.shields.io/badge/Purpose-Educational-orange)

---

## Overview

This project presents the design, implementation, and cryptanalysis of a **Simplified Advanced Encryption Standard (S-AES)** operating in **Cipher Block Chaining (CBC) mode**.

The system is fully implemented in **Python without using any predefined cryptographic libraries**, ensuring a complete and transparent understanding of how symmetric encryption works internally.

The project demonstrates:
- How block ciphers are structured
- How CBC mode improves security
- How cryptanalysis techniques can be used to break weak encryption systems

The system supports:
- Text encryption/decryption  
- Image encryption/decryption  
- Video encryption/decryption  

All inputs are converted into binary and processed using a **fixed 16-bit block size**.

---

## Project Objectives

The main goals of this project are:

- Implement Simplified AES (S-AES) from scratch  
- Apply CBC (Cipher Block Chaining) mode  
- Build a full encryption–decryption pipeline  
- Perform cryptanalysis (brute force & known-plaintext attacks)  
- Simulate realistic attack scenarios  

---

## Project Methodology

The project is structured into four main phases:

---

### Phase 1: Theoretical Study

This phase focused on understanding core cryptographic concepts:

- Simplified AES (S-AES)
- Substitution–Permutation Networks (SPN)
- CBC mode of operation
- Cryptanalysis techniques:
  - Brute force attack
  - Known-plaintext attack

**Key Insight:**
> A 16-bit key produces only 65,536 possible keys, making brute force attacks practical.

---

### Phase 2: System Implementation

The system was implemented using a modular architecture.

#### Project Structure

```
SAES_CBC_Project/
│
├── src/
│   ├── saes.py           # Core S-AES algorithm
│   ├── cbc.py            # CBC mode implementation
│   ├── bruteforce.py     # Brute force attack
│   ├── utils.py          # Binary & file processing
│   ├── step4_attack.py   # External ciphertext attack
│   └── main.py           # Execution script
```

---

## Cryptographic Design

### 1. Simplified AES (S-AES)

- Block size: **16 bits**
- Key size: **16 bits**

Core operations:

- **SubNib (S-Box)** → provides *confusion*  
- **ShiftRows** → provides *diffusion*  
- **AddRoundKey (XOR)** → integrates the key  
- **Key Expansion** → generates round keys  

**Insight:**
> Confusion and diffusion are essential to hide patterns and secure data.

---

### 2. CBC Mode of Operation

CBC introduces dependency between blocks.

#### Encryption

```
C0 = E(P0 XOR IV)
Ci = E(Pi XOR Ci-1)
```

#### Decryption

```
P0 = D(C0) XOR IV
Pi = D(Ci) XOR Ci-1
```

**Key Properties:**

- Prevents identical plaintext → identical ciphertext  
- Introduces chaining dependency  
- Uses Initialization Vector (IV)  

**Important Insight:**
> Different IVs produce different ciphertexts even for the same plaintext.

---



## Phase 3: Cryptanalysis (Brute Force Attack)

An exhaustive key search was implemented:

- Tests all 65,536 possible keys  
- Decrypts ciphertext for each key  
- Compares with known plaintext  

**Result:**
```
Key found: 1010011100111011
```

**Critical Insight:**
> Small key sizes make brute force attacks feasible.

---

## Phase 4: External Ciphertext Attack (Step 4)

A **known-plaintext attack** was applied to external ciphertext.

**Scenario:**
- Partial ciphertext is available  
- Partial plaintext is known  
- Goal: recover the key  

**Result:**
```
KEY RECOVERED SUCCESSFULLY
Recovered Key: 1010011100111011
```

**Key Insight:**
> Even partial plaintext significantly reduces attack complexity.

---

## Data Processing Pipeline

1. Input (text/image/video)  
2. Convert to binary  
3. Split into 16-bit blocks  
4. Apply CBC XOR preprocessing  
5. Encrypt using S-AES  
6. Generate ciphertext  
7. Decrypt using reverse operations  
8. Reconstruct original data  
---
## Code Implementation (Detailed Function Documentation)

This section explains the internal implementation of the S-AES CBC cryptographic system. It describes how each Python module works and how the encryption, decryption, and attack processes are performed step by step.

---

## 1. Core S-AES Implementation (saes.py)

The `saes.py` file contains the main implementation of the Simplified AES algorithm. This module is responsible for encrypting and decrypting 16-bit data blocks using a symmetric key.

### S-Box Substitution

The `sub_nibbles` function divides each 16-bit block into four 4-bit segments and replaces each segment using a predefined substitution box. This operation introduces non-linearity into the encryption process, which improves security by making the relationship between plaintext and ciphertext more complex.

The inverse function `inv_sub_nibbles` performs the opposite operation during decryption. It uses the inverse S-Box to restore the original values of each 4-bit segment.
```
SBOX = {
    "0000": "1110", "0001": "0100", "0010": "1101", "0011": "0001",
    "0100": "0010", "0101": "1111", "0110": "1011", "0111": "1000",
    "1000": "0011", "1001": "1010", "1010": "0110", "1011": "1100",
    "1100": "0101", "1101": "1001", "1110": "0000", "1111": "0111"
}

INV_SBOX = {v: k for k, v in SBOX.items()}


def sub_nibbles(block):
    return ''.join(SBOX[block[i:i+4]] for i in range(0, 16, 4))


def inv_sub_nibbles(block):
    return ''.join(INV_SBOX[block[i:i+4]] for i in range(0, 16, 4))
```
---

### ShiftRows Operation

The `shift_rows` function rearranges the positions of the 4-bit segments inside the 16-bit block. This step increases diffusion by ensuring that small changes in the input affect multiple parts of the output. In this simplified implementation, the inverse operation restores the original arrangement during decryption.
```
def shift_rows(block):
    return block[0:4] + block[12:16] + block[8:12] + block[4:8]


def inv_shift_rows(block):
    return block[0:4] + block[12:16] + block[8:12] + block[4:8]
```
---

### AddRoundKey Operation

The `add_round_key` function performs a bitwise XOR operation between the data block and the encryption key. This is one of the most important steps in the algorithm because it ensures that the encryption process is directly dependent on the secret key.
```
def add_round_key(block, key):
    return xor(block, key)
```
The XOR operation used in this function is implemented in the `utils.py` module and is reused across the system for both encryption and CBC chaining.
---

### Key Expansion

The `key_expansion` function generates three different round keys from the original 16-bit key. Each round key is used at a different stage of encryption. This simulates the key schedule process used in real AES systems, although in a simplified form.
```
def key_expansion(key):
    return [
        key,
        xor(key, "1010101010101010"),
        xor(key, "0101010101010101")
    ]

```
---

### Encryption Process

The `encrypt_block` function applies multiple transformation steps to a 16-bit plaintext block. First, the block is combined with the first round key using XOR. Then substitution and shifting operations are applied to introduce confusion and diffusion. After that, additional rounds of substitution and XOR operations are performed using the remaining round keys. The final output is the ciphertext block.
```
def encrypt_block(block, key):
    k = key_expansion(key)

    state = add_round_key(block, k[0])
    state = sub_nibbles(state)
    state = shift_rows(state)

    state = add_round_key(state, k[1])
    state = sub_nibbles(state)

    state = add_round_key(state, k[2])

    return state
```
---

### Decryption Process

The `decrypt_block` function reverses the encryption steps in the correct order. It starts by applying the last round key, followed by inverse substitution and inverse shifting operations. Then it continues reversing each transformation until the original plaintext block is fully recovered.
```
def decrypt_block(block, key):
    k = key_expansion(key)

    state = add_round_key(block, k[2])
    state = inv_sub_nibbles(state)

    state = add_round_key(state, k[1])
    state = inv_shift_rows(state)

    state = inv_sub_nibbles(state)

    state = add_round_key(state, k[0])

    return state
```
---

## 2. CBC Mode Implementation (cbc.py)

The `cbc.py` file implements the Cipher Block Chaining (CBC) mode of operation. This mode improves security by linking each block of data to the previous one.

Note: Zero padding is used to ensure that all data fits into 16-bit blocks. During decryption, padding is not explicitly removed, which is acceptable for this educational implementation.
---

### Encryption Process

The `encrypt_cbc` function processes each plaintext block sequentially. Before encryption, each block is XORed with the previous ciphertext block. For the first block, the Initialization Vector (IV) is used instead. The result is then encrypted using the S-AES algorithm. After each iteration, the newly generated ciphertext becomes the reference for the next block.

This chaining mechanism ensures that identical plaintext blocks produce completely different ciphertext outputs.
```
def encrypt_cbc(blocks, key, iv):
    ciphertext = []
    prev = iv

    for block in blocks:
        block = block[:16].ljust(16, '0')
        prev = prev[:16].ljust(16, '0')

        xored = xor(block, prev)
        encrypted = encrypt_block(xored, key)

        ciphertext.append(encrypted)
        prev = encrypted

    return ciphertext
```
---

### Decryption Process

The `decrypt_cbc` function reverses the CBC encryption process. Each ciphertext block is first decrypted using S-AES. Then the result is XORed with the previous ciphertext block (or IV for the first block). This restores the original plaintext. After each step, the current ciphertext block is stored for use in the next iteration.
```
def decrypt_cbc(ciphertext_blocks, key, iv):
    plaintext = []
    prev = iv

    for block in ciphertext_blocks:
        block = block[:16].ljust(16, '0')

        decrypted = decrypt_block(block, key)
        plain = xor(decrypted, prev)

        plaintext.append(plain)
        prev = block

    return plaintext
```
---

## 3. Brute Force Attack (bruteforce.py)

The `brute_force` function attempts to recover the secret key by testing all possible 16-bit key combinations. Since the key space contains 65,536 possible values, the function iterates through every possible key.

For each key, the ciphertext is decrypted using the CBC decryption function. The result is then compared with the known original plaintext. If a match is found, the correct key is identified and returned immediately.

This implementation clearly demonstrates that small key sizes make exhaustive search attacks computationally feasible and efficient.
```
def brute_force(ciphertext, iv, original_blocks):
    target = original_blocks

    for key in range(65536):
        key_bin = format(key, '016b')

        decrypted = decrypt_cbc(ciphertext, key_bin, iv)

        if decrypted[:len(target)] == target:
            print("Key found:", key_bin)
            return key_bin

    print("Key not found")
    return None
```
---

## 4. External Ciphertext Attack (step4_attack.py)

The `attack_other_group` function simulates a known-plaintext attack scenario on external ciphertext. In this case, the attacker has access to a portion of ciphertext and a corresponding portion of plaintext.

The function tries all possible keys and decrypts the ciphertext using each one. It then compares the decrypted output with the known plaintext. If both match, the correct encryption key is recovered.

This attack demonstrates how partial knowledge of plaintext can significantly reduce the difficulty of breaking encryption systems with small key sizes.
```
def attack_other_group(ciphertext, iv, known_plaintext):
    print("\n[ STEP 4 ATTACK STARTED ]")

    for key in range(65536):
        key_bin = format(key, '016b')

        decrypted_blocks = decrypt_cbc(ciphertext, key_bin, iv)

        if decrypted_blocks == known_plaintext:
            print("\n✔ KEY RECOVERED SUCCESSFULLY")
            print("Recovered Key:", key_bin)
            return key_bin

    print("Key not found")
    return None
```
---

## 5. Utility Functions (utils.py)

The `utils.py` file contains helper functions that support data processing throughout the system.

The XOR function performs bitwise comparison between two binary strings and is used in both encryption and CBC chaining.

The text conversion functions transform readable text into binary format and back into text after decryption. This allows the encryption system to process human-readable input.

The block splitting function divides binary data into fixed 16-bit blocks and adds padding when necessary to ensure consistency.

The file conversion functions allow images and videos to be converted into binary format for encryption and then reconstructed back into their original form after decryption.
```
def xor(a, b):
    return ''.join('1' if x != y else '0' for x, y in zip(a, b))

def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)

def split_blocks(binary, size=16):
    # padding first
    while len(binary) % size != 0:
        binary += '0'

    return [binary[i:i+size] for i in range(0, len(binary), size)]

def file_to_binary(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return ''.join(format(byte, '08b') for byte in data)


def binary_to_file(binary, output_path):
    bytes_list = [binary[i:i+8] for i in range(0, len(binary), 8)]
    byte_data = bytearray(int(b, 2) for b in bytes_list)

    with open(output_path, "wb") as f:
        f.write(byte_data)

def pad16(binary):
    while len(binary) % 16 != 0:
        binary += '0'
    return binary

def safe16(block):
    return block[:16].ljust(16, '0')
```
---

## 6. Main Execution File (main.py)

The `main.py` file acts as the central controller of the system. It connects all modules together and executes the full encryption and decryption pipeline.

First, it converts plaintext into binary format and splits it into blocks. Then it encrypts the data using CBC mode and decrypts it to verify correctness. After that, it performs a brute force attack to recover the encryption key.

The system is also tested on image and video files by converting them into binary format, encrypting them, and reconstructing them after decryption. Finally, an external ciphertext attack is executed to simulate a real-world cryptanalysis scenario.
```
plaintext = "HELLO"
key = "1010011100111011"
iv = "1100101011110001"


# -------------------------
# TEXT TEST
# -------------------------
binary = text_to_binary(plaintext)
blocks = split_blocks(binary)

print("Binary blocks:", blocks)

ciphertext = encrypt_cbc(blocks, key, iv)
print("Ciphertext:", ciphertext)

decrypted_blocks = decrypt_cbc(ciphertext, key, iv)
decrypted_text = binary_to_text("".join(decrypted_blocks))

print("Decrypted:", decrypted_text)


# FIXED BRUTE FORCE CALL
print("\n--- BRUTE FORCE ---")
brute_force(ciphertext, iv, blocks[:len(blocks)])


# -------------------------
# IMAGE TEST
# -------------------------
print("\n--- IMAGE TEST ---")

image_path = "../assets/image.png"
output_path = "../decrypted_image.png"

binary_image = file_to_binary(image_path)
image_blocks = split_blocks(binary_image)

cipher_image = encrypt_cbc(image_blocks, key, iv)
decrypted_image_blocks = decrypt_cbc(cipher_image, key, iv)

binary_to_file("".join(decrypted_image_blocks), output_path)

print("Image encryption done.")


# -------------------------
# VIDEO TEST
# -------------------------
print("\n--- VIDEO TEST ---")

video_path = "../assets/video.mp4"
output_video_path = "../decrypted_video.mp4"

binary_video = file_to_binary(video_path)
video_blocks = split_blocks(binary_video)

cipher_video = encrypt_cbc(video_blocks, key, iv)
decrypted_video_blocks = decrypt_cbc(cipher_video, key, iv)

binary_to_file("".join(decrypted_video_blocks), output_video_path)

print("Video encryption done.")


# -------------------------
# STEP 4 ATTACK
# -------------------------
print("\n--- STEP 4 ---")

other_ciphertext = cipher_image[:3]
other_iv = iv
known_plaintext = image_blocks[:3]

attack_other_group(other_ciphertext, other_iv, known_plaintext)
```
---

## Summary of Code Behavior

This implementation successfully demonstrates a full cryptographic system that includes encryption, decryption, and attack simulation. All modules work together to process different types of data, including text, images, and videos.

The system correctly applies CBC mode to improve security, but the cryptanalysis results clearly show that the small key size makes the system vulnerable to brute force and known-plaintext attacks.


---
## Compliance with Project Requirements

This implementation strictly follows the project constraints:
- No predefined cryptographic libraries were used
- All encryption, decryption, and attack logic were implemented from scratch in Python

---

## System Validation

### Example Execution Output

```
Plaintext: HELLO

Binary blocks:
['0100100001000101', '0100110001001100', '0100111100000000']

Ciphertext:
['0110010000001110', '1110101000100101', '1111101111111011']

Decrypted:
HELLO

--- BRUTE FORCE ---
Key found: 1010011100111011

--- STEP 4 ---
KEY RECOVERED SUCCESSFULLY
```

**Validation confirms:**
- Correct encryption and decryption  
- Proper CBC chaining behavior  
- Successful key recovery  

---

## Security Analysis

### Strengths
- Correct S-AES implementation  
- Proper CBC chaining  
- Supports multiple data types  
- Demonstrates confusion & diffusion  

### Weaknesses
- Very small key size (16-bit)  
- Vulnerable to brute force attacks  
- Vulnerable to known-plaintext attacks  

---

## Critical Security Insights

### 1. CBC vs Key Strength
> CBC removes patterns but does NOT prevent brute force attacks.

### 2. Importance of Key Size
> Security depends heavily on key size. Small keys are easily breakable.

### 3. Known-Plaintext Risk
> Partial plaintext knowledge significantly reduces attack complexity.

### 4. Role of IV
> IV ensures randomness and prevents repeated ciphertext.

### 5. Error Propagation
> A corrupted ciphertext block affects multiple decrypted blocks.

### 6. Educational Limitation of S-AES
> S-AES is designed for learning and does not provide real-world security.

---

## Key Findings

- Encryption system is fully functional  
- CBC mode eliminates plaintext patterns  
- System correctly processes text, images, and video  
- Key recovery is easily achievable  

**Recovered Key:**
```
1010011100111011
```

---

## Requirements

- Python 3.10+
- No external libraries required

---

## Quick Start

```bash
git clone https://github.com/GhadeerZahwe/saes-cbc-cryptography-project
cd saes-cbc-cryptography-project/src
python main.py
```

---

## Educational Value

This project demonstrates:

- How encryption algorithms work internally  
- How block cipher modes affect security  
- How cryptanalysis breaks weak systems  
- Why strong key sizes are essential  

---

## Limitations

- S-AES is a simplified educational model  
- 16-bit key size is insecure  
- No MixColumns operation  
- Not suitable for real-world security  

---

## Recommendations

- Use larger key sizes (AES-128 or higher)  
- Use standard cryptographic algorithms  
- Ensure secure IV handling  
- Combine encryption with authentication (MAC / AEAD)  

---

## Future Work

- Full AES implementation (including MixColumns)  
- Additional modes (CTR, GCM, OFB)  
- Performance optimization  
- GUI development  
- Real-time encryption systems  

---

## Repository

This repository contains:
- Full source code (S-AES, CBC, attacks)
- Testing scripts
- Sample data (text, image, video)
- Complete project documentation

GitHub:
https://github.com/GhadeerZahwe/saes-cbc-cryptography-project  

---

## Conclusion

This project demonstrates the complete lifecycle of a cryptographic system:

- Design  
- Implementation  
- Encryption & Decryption  
- Cryptanalysis  

### Final Insight

A secure cryptographic system depends on:

- A strong algorithm  
- A secure mode of operation  
- A sufficiently large key size  

> Even with a correct implementation, a weak key size compromises the entire system.
