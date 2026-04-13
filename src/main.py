from utils import text_to_binary, binary_to_text, split_blocks
from cbc import encrypt_cbc, decrypt_cbc
from bruteforce import brute_force

plaintext = "HELLO"
key = "1010011100111011"
iv = "1100101011110001"

# Convert to binary
binary = text_to_binary(plaintext)

# Split into blocks
blocks = split_blocks(binary)

print("Binary blocks:", blocks)

# Encrypt
ciphertext = encrypt_cbc(blocks, key, iv)
print("Ciphertext:", ciphertext)

# Decrypt
decrypted_blocks = decrypt_cbc(ciphertext, key, iv)

# Convert back to text
decrypted_binary = ''.join(decrypted_blocks)
decrypted_text = binary_to_text(decrypted_binary)

print("Decrypted:", decrypted_text)

# Brute force attack
brute_force(ciphertext, iv, blocks)

print("\n--- IMAGE TEST ---")

image_path = "../image.png"
output_path = "../decrypted_image.png"

# Convert image to binary
binary_image = file_to_binary(image_path)

# Split into blocks
image_blocks = split_blocks(binary_image)

# Encrypt
cipher_image = encrypt_cbc(image_blocks, key, iv)

# Decrypt
decrypted_blocks = decrypt_cbc(cipher_image, key, iv)

# Convert back to binary
decrypted_binary = ''.join(decrypted_blocks)

# Save reconstructed image
binary_to_file(decrypted_binary, output_path)

print("Image encryption and decryption completed.")