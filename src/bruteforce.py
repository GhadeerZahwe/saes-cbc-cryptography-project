from cbc import decrypt_cbc

def brute_force(ciphertext, iv, original_blocks):
    target = original_blocks

    for key in range(65536):
        key_bin = format(key, '016b')

        decrypted = decrypt_cbc(ciphertext, key_bin, iv)

       

    print("Key not found")
    return None