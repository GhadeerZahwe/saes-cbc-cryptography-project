from utils import xor
from saes import encrypt_block, decrypt_block



def decrypt_cbc(ciphertext_blocks, key, iv):
    plaintext = []
    prev = iv

    for block in ciphertext_blocks:
        decrypted = decrypt_block(block, key)
        plain_block = xor(decrypted, prev)
        plaintext.append(plain_block)
        prev = block

    return plaintext