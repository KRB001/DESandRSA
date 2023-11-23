from convert import *
from subkeys import *
from message_manipulation import *
from read import *
table_reader = read.TableReader()
import binascii

def encrypt(message, key):
    result = ""
    length = len(message) // 8
    residual = len(message) % 8

    for i in range(length):
        result = result + encrypt_block(message[i*8:i*8+8], key)

    # pad the last block if less than 8 bytes
    if residual > 0:
        final_block = message[length*8:length*8+residual]
        for i in range(8 - residual):
            final_block = final_block + "-"

        result = result + encrypt_block(final_block, key)

    return result

def decrypt(message, key):
    result = ""
    length = len(message) // 18

    for i in range(length):
        result = result + decrypt_block(message[i*18:i*18+18], key)

    return result.strip("-")

def encrypt_block(message, key):
    key = ascii_to_binary(key)
    message = ascii_to_binary(message)

    pc1 = permute(table_reader.get_pc1(), key)
    c0 = pc1[0:28]
    d0 = pc1[28:56]

    c_blocks = get_blocks(c0)
    d_blocks = get_blocks(d0)

    subkeys = calculate_subkeys(c_blocks, d_blocks)

    ip = permute(table_reader.get_ip(), message)

    lr_blocks = get_lr_blocks(ip[0:32], ip[32:64], subkeys)
    ground_message = lr_blocks[1] + lr_blocks[0]

    return hex(int(permute(table_reader.get_ip1(), ground_message), 2))

def decrypt_block(message, key):
    key = ascii_to_binary(key)
    message = hex_to_binary(message)

    pc1 = permute(table_reader.get_pc1(), key)
    c0 = pc1[0:28]
    d0 = pc1[28:56]

    c_blocks = get_blocks(c0)
    d_blocks = get_blocks(d0)

    subkeys = calculate_subkeys(c_blocks, d_blocks)

    ip_flipped = permute(table_reader.get_ip(), message)

    ip = ip_flipped[32:64] + ip_flipped[0:32]

    lr_blocks = get_lr_blocks(ip[0:32], ip[32:64], subkeys[::-1])

    result_bin = permute(table_reader.get_ip1(), lr_blocks[0] + lr_blocks[1])

    return int(result_bin, 2).to_bytes((int(result_bin, 2).bit_length() + 7) // 8, 'big').decode()