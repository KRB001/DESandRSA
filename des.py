from convert import *
from subkeys import *
from message_manipulation import *
from read import *
table_reader = read.TableReader()

def encrypt(message, key):
    key = table_reader.get_key()
    result = ""
    message = ascii_to_binary(message)

    pc1 = permute(table_reader.get_pc1(), key)
    c0 = pc1[0:28]
    d0 = pc1[29:56]

    c_blocks = get_blocks(c0)
    d_blocks = get_blocks(d0)

    subkeys = calculate_subkeys(c_blocks, d_blocks)

    ip = permute(table_reader.get_ip(), message)

    return result