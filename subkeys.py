import read
table_reader = read.TableReader()
pc1_table = table_reader.get_pc1()
pc2_table = table_reader.get_pc2()
shifts = table_reader.get_c_d_shifts()


def pc1_permute(key):
    pc1 = ""
    for r in range(len(pc1_table)):
        for c in range(len(pc1_table[r])):
            pc1 = pc1 + (key[int(pc1_table[r][c]) - 1])

    return pc1

def left_shift(message):
    first = message[0]
    result = message[1:]
    result = result + first
    return result

def get_blocks(block):
    current = block
    blocks = []
    for shift in shifts:
        for i in range(int(shift)):
            current = left_shift(current)
        blocks.append(current)

    return blocks

def pc2_permute(pair):
    subkey = ""
    for r in range(len(pc2_table)):
        for c in range(len(pc2_table[r])):
            subkey = subkey + (pair[int(pc2_table[r][c]) - 1])
    return subkey

def calculate_subkeys(c_blocks,d_blocks):
    subkeys = []
    for i in range(len(c_blocks)):
        cd_pair = c_blocks[i] + d_blocks[i]
        subkey = pc2_permute(cd_pair)
        subkeys.append(subkey)
    return subkeys



