import sys
try:
    from PIL import Image
    im = Image.open('logo.jpg').convert('RGB')
    im = im.resize((50, 50))
    pixels = im.getcolors(2500)
    sorted_pixels = sorted(pixels, key=lambda t: t[0], reverse=True)
    for count, color in sorted_pixels:
        r, g, b = color
        if max(r,g,b) - min(r,g,b) < 30: continue
        if sum((r,g,b)) < 60: continue
        print(f"Colorful Dominant: #{r:02x}{g:02x}{b:02x} ({count} pixels)")
except ImportError:
    pass
