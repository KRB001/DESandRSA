from convert import *
from subkeys import *

def encrypt(message, key):
    result = ""
    message = ascii_to_binary(message)

    pc1 = pc1_permute(key)
    c0 = pc1[0:27]
    d0 = pc1[28:55]

    c_blocks = get_blocks(c0)
    d_blocks = get_blocks(d0)

    subkeys = calculate_subkeys(c_blocks, d_blocks)

    return result