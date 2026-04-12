def xor(a, b):
    return ''.join('1' if x != y else '0' for x, y in zip(a, b))

def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

def split_blocks(binary, size=16):
    return [binary[i:i+size] for i in range(0, len(binary), size)]