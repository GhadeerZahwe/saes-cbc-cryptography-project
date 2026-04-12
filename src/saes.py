def sub_nib(state):
    return [S_BOX[n] for n in state]

def shift_rows(state):
    return [state[0], state[1], state[3], state[2]]

def mix_columns(state):
    return [
        state[0] ^ state[2],
        state[1] ^ state[3],
        state[2] ^ state[0],
        state[3] ^ state[1]
    ]

def add_round_key(state, key):
    return [s ^ k for s, k in zip(state, key)]

def key_expansion(key):
    return key, key  # simplified version for implementation

def encrypt_block(block, key):
    state = add_round_key(block, key)
    state = sub_nib(state)
    state = shift_rows(state)
    state = mix_columns(state)
    state = add_round_key(state, key)
    return state

def decrypt_block(block, key):
    state = add_round_key(block, key)
    state = mix_columns(state)
    state = shift_rows(state)
    state = sub_nib(state)
    state = add_round_key(state, key)
    return state