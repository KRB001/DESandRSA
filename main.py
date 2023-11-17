import read
from subkeys import *
from convert import *
from read import TableReader
table_reader = read.TableReader()

key = table_reader.get_key()
print(key)
pc1 = pc1_permute(key)
print(pc1)
c0 = pc1[0:28]
d0 = pc1[28:56]
print(c0)
print(d0)

print(get_blocks(c0))
print(get_blocks(d0))