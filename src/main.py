from utils import (
    text_to_binary,
    binary_to_text,
    split_blocks,
    file_to_binary,
    binary_to_file
)

from cbc import encrypt_cbc, decrypt_cbc
from bruteforce import brute_force
from step4_attack import attack_other_group


plaintext = "HELLO"         # The plaintext we want to encrypt and later use for the brute-force attack.
key = "1010011100111011"    # The 16-bit key used for encryption and decryption. This key will be the target of our brute-force attack.
iv = "1100101011110001"     # The Initialization Vector (IV) used in CBC mode. It should be random and unique for each encryption operation, but for testing purposes, we are using a fixed IV.


# -------------------------
# TEXT TEST
# -------------------------
binary = text_to_binary(plaintext)                  # Converts the plaintext string "HELLO" into its binary representation. Each character is represented by its ASCII value in binary
blocks = split_blocks(binary)                       # Cuts binary into 16-bit chunks # Splits the binary string into blocks of 16 bits (4 characters). This is necessary because our encryption algorithm operates on fixed-size blocks.

print("Binary blocks:", blocks)

ciphertext = encrypt_cbc(blocks, key, iv)           # Encrypts the blocks using CBC mode = Lock the message using the secret key
print("Ciphertext:", ciphertext)

decrypted_blocks = decrypt_cbc(ciphertext, key, iv) # Unlocks the ciphertext using the same key = Unlock the message with the secret key
decrypted_text = binary_to_text("".join(decrypted_blocks))

print("Decrypted:", decrypted_text)


# FIXED BRUTE FORCE CALL
print("\n--- BRUTE FORCE ---")
brute_force(ciphertext, iv, blocks[:len(blocks)]) # Calls the brute force attack function


# -------------------------
# IMAGE TEST
# -------------------------
print("\n--- IMAGE TEST ---")

image_path = "../assets/image.png"
output_path = "../decrypted_image.png"

binary_image = file_to_binary(image_path)
image_blocks = split_blocks(binary_image)

cipher_image = encrypt_cbc(image_blocks, key, iv)
decrypted_image_blocks = decrypt_cbc(cipher_image, key, iv)

binary_to_file("".join(decrypted_image_blocks), output_path)

print("Image encryption done.")


# -------------------------
# VIDEO TEST
# -------------------------
print("\n--- VIDEO TEST ---")

video_path = "../assets/video.mp4"
output_video_path = "../decrypted_video.mp4"

binary_video = file_to_binary(video_path)
video_blocks = split_blocks(binary_video)

cipher_video = encrypt_cbc(video_blocks, key, iv)
decrypted_video_blocks = decrypt_cbc(cipher_video, key, iv)

binary_to_file("".join(decrypted_video_blocks), output_video_path)

print("Video encryption done.")


# -------------------------
# STEP 4 ATTACK
# -------------------------
print("\n--- STEP 4 ---")

other_ciphertext = cipher_image[:3]  # First 3 encrypted blocks
other_iv = iv                        # Same IV
known_plaintext = image_blocks[:3]   # First 3 original blocks

attack_other_group(other_ciphertext, other_iv, known_plaintext) # Calls the known-plaintext attack

# here we Creates a scenario where we only know PART of the data that was encrypted (the first 3 blocks of the image) and we want to find the key used for encryption by trying all possible keys and checking if the decrypted output matches the known plaintext.