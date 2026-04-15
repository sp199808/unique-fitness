import sys
from collections import Counter
try:
    from PIL import Image
    im = Image.open('logo.jpg').convert('RGB')
    im = im.resize((50, 50))
    pixels = im.getcolors(2500)
    sorted_pixels = sorted(pixels, key=lambda t: t[0], reverse=True)
    for p in sorted_pixels:
        count, color = p
        r,g,b = color
        if (r > 220 and g > 220 and b > 220) or (r < 30 and g < 30 and b < 30):
             continue
        print(f"Dominant color: #{r:02x}{g:02x}{b:02x}")
        break
except ImportError:
    print("Pillow not installed")
