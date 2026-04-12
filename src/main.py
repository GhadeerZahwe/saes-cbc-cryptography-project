plaintext = "HELLO"
key = "1010011100111011"
iv = "1100101011110001"

binary = text_to_binary(plaintext)
blocks = split_blocks(binary)

ciphertext = encrypt_cbc(blocks, key, iv)
decrypted = decrypt_cbc(ciphertext, key, iv)

print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted)