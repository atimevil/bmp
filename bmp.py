import struct
width = 128
height = 128
bpp = 24
pixel_data_size = width * height * (bpp // 8)
file_size = 54 + pixel_data_size

bmp_header = bytearray([
    0x42, 0x4D
])
bmp_header += struct.pack('<I', file_size)
bmp_header += b'\x00\x00\x00\x00'
bmp_header += struct.pack('<I', 54)
bmp_header += struct.pack('<I', 40)
bmp_header += struct.pack('<I', width)
bmp_header += struct.pack('<I', height)
bmp_header += struct.pack('<H', 1)
bmp_header += struct.pack('<H', bpp)
bmp_header += b'\x00\x00\x00\x00'
bmp_header += struct.pack('<I', pixel_data_size)
bmp_header += b'\x00\x00\x00\x00' * 4

pattern = b''
for i in range(pixel_data_size):
    pattern += bytes([0x41 + (i % 26)]) 

with open('pattern_seh.bmp', 'wb') as f:
    f.write(bmp_header)
    f.write(pattern)
