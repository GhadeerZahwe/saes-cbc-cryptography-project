from cbc import decrypt_cbc

def attack_other_group(ciphertext, iv, known_plaintext):
    print("\n[ STEP 4 ATTACK STARTED ]")

    for key in range(65536):
        key_bin = format(key, '016b')

        decrypted_blocks = decrypt_cbc(ciphertext, key_bin, iv)

       
    print("Key not found")
    return None