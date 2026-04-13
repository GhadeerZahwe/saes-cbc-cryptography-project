def xor(a, b):
    return ''.join('1' if x != y else '0' for x, y in zip(a, b))

def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)

def split_blocks(binary, size=16):
    while len(binary) % size != 0:
        binary += '0'   # padding
    return [binary[i:i+size] for i in range(0, len(binary), size)]

def file_to_binary(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return ''.join(format(byte, '08b') for byte in data)

def binary_to_file(binary, output_path):
    bytes_list = [binary[i:i+8] for i in range(0, len(binary), 8)]
    byte_data = bytearray(int(b, 2) for b in bytes_list)
    
    with open(output_path, "wb") as f:
        f.write(byte_data)