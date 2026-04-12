def encrypt_cbc(blocks, key, iv):
    ciphertext = []
    prev = iv

    for block in blocks:
        xored = xor(block, prev)
        encrypted = encrypt_block(xored, key)
        ciphertext.append(encrypted)
        prev = encrypted

    return ciphertext

def decrypt_cbc(ciphertext_blocks, key, iv):
    plaintext = []
    prev = iv

    for block in ciphertext_blocks:
        decrypted = decrypt_block(block, key)
        plain_block = xor(decrypted, prev)
        plaintext.append(plain_block)
        prev = block

    return plaintext