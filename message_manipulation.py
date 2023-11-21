from subkeys import permute
import read
table_reader = read.TableReader()


def get_lr_blocks(l0, r0, subkeys):
    l_block = r0
    r_block = xor(l0, grind(r0, subkeys[0]))

    for i in range(len(subkeys) - 1):
        temp = l_block
        l_block = r_block
        r_block = xor(temp, grind(r0, subkeys[i + 1]))

    return [l_block, r_block]

def xor(a, b):
    result = ""
    for bit in range(len(a)):
        result = result + str((int(a[bit]) + int(b[bit])) % 2)
    return result

def grind(r0, subkey):
    s_tables = table_reader.get_s_tables()
    r0_expand = permute(table_reader.get_e(), r0)
    r0_xor = xor(r0_expand, subkey)
    result = ""

    for i in range(8):
        bit = (i + 1) * 6

        row_dec = r0_xor[bit - 6] + r0_xor[bit - 1]
        row = int(row_dec, 2)

        column_dec = r0_xor[bit-5:bit-1]
        column = int(column_dec, 2)

        s_number = s_tables[i][row][column]
        #print("Chunk " + str(i) +
        #      ": Row " + str(row_dec) + " / " + str(row) +
        #      ", Column " + str(column_dec) + " / " + str(column)
        #      + " / VALUE: " + str(s_number)
        #)

        result = result + str(bin(int(s_number))[2:].zfill(4))

    return permute(table_reader.get_p(), result)