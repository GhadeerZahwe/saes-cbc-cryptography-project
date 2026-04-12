def brute_force(ciphertext, iv, original_plaintext):
    for key in range(65536):
        key_bin = format(key, '016b')
        decrypted = decrypt_cbc(ciphertext, key_bin, iv)

        if decrypted == original_plaintext:
            print("Key found:", key_bin)
            return key_bin