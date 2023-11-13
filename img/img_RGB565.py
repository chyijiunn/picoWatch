from io import BytesIO
from PIL import Image
import sys

if len(sys.argv) > 1:
    path_to_image = str(sys.argv[1])
    x = int(sys.argv[2])
    y = int(sys.argv[3])

    im = Image.open(path_to_image).convert('RGB')  # Convert to RGB
    im_resize = im.resize((x, y))

    # Convert RGB image to RGB565
    rgb565_data = []
    for r, g, b in im_resize.getdata():
        rgb565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
        rgb565_data.extend([rgb565 >> 8, rgb565 & 0xFF])

    byte_im = bytes(rgb565_data)
    print(byte_im)
else:
    print("Please specify the location of the image, i.e., img2bytearray.py /path/to/image width height")
