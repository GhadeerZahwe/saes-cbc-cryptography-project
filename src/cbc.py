def encrypt_cbc(blocks, key, iv):
    ciphertext = []
    prev = iv

    for block in blocks:
        xored = xor(block, prev)
        encrypted = encrypt_block(xored, key)
        ciphertext.append(encrypted)
        prev = encrypted

    return ciphertext