def xor(a, b):
    return ''.join('1' if x != y else '0' for x, y in zip(a, b))

def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)