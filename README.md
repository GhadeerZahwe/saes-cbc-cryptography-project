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
