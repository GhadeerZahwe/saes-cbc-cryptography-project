from cbc import decrypt_cbc

def attack_other_group(ciphertext, iv, known_plaintext): #ciphertext = The encrypted data, iv = Initialization Vector, known_plaintext = The plaintext we know
    print("\n[ STEP 4 ATTACK STARTED ]")

    for key in range(65536): # looping from 0 to 65535 (16-bit key space)
        key_bin = format(key, '016b') # Converts the number (0-65535) into a 16-bit binary string

        decrypted_blocks = decrypt_cbc(ciphertext, key_bin, iv) # Decrypts the ciphertext using the current key and IV, returning the decrypted plaintext

        if decrypted_blocks == known_plaintext: # Compares the decrypted plaintext with the known plaintext. If they match, it means we've found the correct key.
            print("\n✔ KEY RECOVERED SUCCESSFULLY")
            print("Recovered Key:", key_bin)
            return key_bin

    print("Key not found")
    return None