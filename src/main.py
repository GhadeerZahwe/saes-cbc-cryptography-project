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


plaintext = "HELLO"
key = "1010011100111011"
iv = "1100101011110001"


# -------------------------
# TEXT TEST
# -------------------------
binary = text_to_binary(plaintext)
blocks = split_blocks(binary)

print("Binary blocks:", blocks)

ciphertext = encrypt_cbc(blocks, key, iv)
print("Ciphertext:", ciphertext)

decrypted_blocks = decrypt_cbc(ciphertext, key, iv)
decrypted_text = binary_to_text("".join(decrypted_blocks))

print("Decrypted:", decrypted_text)


# FIXED BRUTE FORCE CALL
print("\n--- BRUTE FORCE ---")
brute_force(ciphertext, iv, blocks[:len(blocks)])


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

other_ciphertext = cipher_image[:3]
other_iv = iv
known_plaintext = image_blocks[:3]

attack_other_group(other_ciphertext, other_iv, known_plaintext)