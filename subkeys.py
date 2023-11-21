import read
table_reader = read.TableReader()
pc1_table = table_reader.get_pc1()
pc2_table = table_reader.get_pc2()
shifts = table_reader.get_c_d_shifts()

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

def permute(table, message):
    subkey = ""
    for r in range(len(table)):
        for c in range(len(table[r])):
            subkey = subkey + (message[int(table[r][c]) - 1])
    return subkey

def calculate_subkeys(c_blocks,d_blocks):
    subkeys = []
    for i in range(len(c_blocks)):
        cd_pair = c_blocks[i] + d_blocks[i]
        subkey = permute(pc2_table, cd_pair)
        subkeys.append(subkey)
    return subkeys



