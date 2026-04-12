from cbc import decrypt_cbc

def brute_force(ciphertext, iv, original_blocks):
    for key in range(65536):
        key_bin = format(key, '016b')
        decrypted = decrypt_cbc(ciphertext, key_bin, iv)

        if decrypted == original_blocks:
            print("Key found:", key_bin)
            return key_bin