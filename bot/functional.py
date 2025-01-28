import os
from PIL import Image


def convert_image(path, new_format):
    with Image.open(path) as im:
        if im.mode == "RGBA":
            im = Image.alpha_composite(Image.new("RGBA", im.size, (255, 255, 255)), im)
            im = im.convert("RGB")

        im.save(f"{os.path.splitext(path)[0]}.{new_format.lower()}", format=new_format)
