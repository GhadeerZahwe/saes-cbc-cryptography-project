from saes import encrypt_block, decrypt_block
from utils import xor

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