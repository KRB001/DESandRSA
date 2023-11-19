from subkeys import permute
import read
table_reader = read.TableReader()

def get_lr_blocks(l0, r0, subkeys):
    l_blocks = [r0]
    r_blocks = [xor(l0, grind(r0, subkeys[0]))]

def xor(a, b):
    result = ""
    for bit in range(len(a)):
        result = result + str((int(a[bit]) + int(b[bit])) % 2)
    return result

def grind(r0, subkey):
    r0_expand = permute(table_reader.get_e(), r0)
    r0_xor = xor(r0_expand, subkey)