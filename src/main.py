from utils import text_to_binary, binary_to_text, split_blocks, file_to_binary, binary_to_file
from cbc import encrypt_cbc, decrypt_cbc
from bruteforce import brute_force
from step4_attack import attack_other_group

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
print("Image binary length:", len(binary_image))
print("Number of blocks:", len(image_blocks))
print("Sample encrypted image blocks:", cipher_image[:5])

print("\n--- VIDEO TEST ---")

video_path = "../video.mp4"
output_video_path = "../decrypted_video.mp4"

# Convert video to binary
binary_video = file_to_binary(video_path)
print("Video binary length:", len(binary_video))

# Split into blocks
video_blocks = split_blocks(binary_video)
print("Number of video blocks:", len(video_blocks))

# Encrypt
cipher_video = encrypt_cbc(video_blocks, key, iv)

# Show sample ciphertext
print("Sample encrypted video blocks:", cipher_video[:5])

# Decrypt
decrypted_video_blocks = decrypt_cbc(cipher_video, key, iv)

# Convert back to binary
decrypted_video_binary = ''.join(decrypted_video_blocks)

# Save reconstructed video
binary_to_file(decrypted_video_binary, output_video_path)

print("Video encryption and decryption completed.")
print("Decrypted video saved as:", output_video_path)

print("\n--- STEP 4: OTHER GROUP ATTACK ---")

# Example "other group ciphertext"
other_ciphertext = cipher_image[:3]  # or fake sample blocks

other_iv = iv

# We assume we know expected structure for testing
known_plaintext = image_blocks[:3]

# Run attack
attack_other_group(other_ciphertext, other_iv, known_plaintext)