from utils import xor

SBOX = {
    "0000": "1110", "0001": "0100", "0010": "1101", "0011": "0001",
    "0100": "0010", "0101": "1111", "0110": "1011", "0111": "1000",
    "1000": "0011", "1001": "1010", "1010": "0110", "1011": "1100",
    "1100": "0101", "1101": "1001", "1110": "0000", "1111": "0111"
}

INV_SBOX = {v: k for k, v in SBOX.items()}


def sub_nibbles(block):
    return ''.join(SBOX[block[i:i+4]] for i in range(0, 16, 4))


def inv_sub_nibbles(block):
    return ''.join(INV_SBOX[block[i:i+4]] for i in range(0, 16, 4))


def shift_rows(block):
    return block[0:4] + block[12:16] + block[8:12] + block[4:8]


def inv_shift_rows(block):
    return block[0:4] + block[12:16] + block[8:12] + block[4:8]


def add_round_key(block, key):
    return xor(block, key)


def key_expansion(key):
    return [
        key,
        xor(key, "1010101010101010"),
        xor(key, "0101010101010101")
    ]


# TODO