import os

# in bits
block_size = 100000
block_num = 10
input_file = 'output1.bin'
from_pos = 'head'
out_dir = 'data-busy'

try:
    os.makedir(out_dir)
except:
    pass

input_data = open(input_file).read()
data_byte_size = len(input_data)
assert data_byte_size * 8 >= block_num * block_size

for i in range(block_num):

    if from_pos == 'tail':

        start = data_byte_size - (i + 1) * block_size / 8
        end = data_byte_size - i * block_size / 8 
        print(start, end)
        data = input_data[start : end]
        # print(len(data), block_size / 8)
        assert len(data) == block_size / 8

    else:

        start = i * block_size / 8
        end = (i + 1) * block_size / 8 
        print(start, end)
        data = input_data[start : end]
        # print(len(data), block_size / 8)
        assert len(data) == block_size / 8

    output = open(os.path.join(out_dir, 'data-%d.txt') % i, 'wb')
    output.write(data)