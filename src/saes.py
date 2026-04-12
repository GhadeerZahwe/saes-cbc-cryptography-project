from utils import xor

def encrypt_block(block, key):
    return xor(block, key)

def decrypt_block(block, key):
    return xor(block, key)