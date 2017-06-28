import struct
valid_png_header = b'\x89PNG\r\n\x1a\n'
data=b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
if data[:8]==valid_png_header:
    weight,height=struct.unpack('>LL',data[16:24])
    print('valid png weight',weight,'hight',height)
else:
    print("not a valid png")

