import struct
import re

def to_binary(data):

    binary = b''
    for i in range(len(data) / 2):
        byte = data[i * 2 : i * 2 + 2]
        assert len(byte) == 2
        byte = int(byte, 16)
        binary += struct.pack('B', byte)

    return binary

log = open('log1.txt').read().splitlines()
output = open('output1.bin', 'wb')

count = 0
size_bytes = 0

# example line: 
# entlog f7d27dc8b85bb032

for line in log:

    if not line.startswith('entlog'):
        continue

    data = line.split()[1]
    output.write(to_binary(data))
    count += 1
    size_bytes += len(data) / 2


output.close()
print('%d log entries, %d bytes (%d bits) data' % (count, size_bytes, 8 * size_bytes) )