import read
table_reader = read.TableReader()
pc1_table = table_reader.get_pc1()
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





