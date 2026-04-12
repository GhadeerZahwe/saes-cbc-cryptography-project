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