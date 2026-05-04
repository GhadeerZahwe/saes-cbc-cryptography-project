from cbc import decrypt_cbc

def brute_force(ciphertext, iv, original_blocks): #ciphertext = The encrypted data, iv = Initialization Vector, original_blocks = The original plaintext blocks we want to match
    target = original_blocks

    for key in range(65536): # looping from 0 to 65535 (16-bit key space)
        key_bin = format(key, '016b') # Converts the number (0-65535) into a 16-bit binary string

        decrypted = decrypt_cbc(ciphertext, key_bin, iv) # Decrypts the ciphertext using the current key and IV, returning the decrypted plaintext

        if decrypted[:len(target)] == target: # Checks if the decrypted plaintext starts with the original plaintext. If it does, it means we've found the correct key.
            print("Key found:", key_bin)
            return key_bin

    print("Key not found")
    return None