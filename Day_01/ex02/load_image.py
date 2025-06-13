import os
import numpy as np
from PIL import Image


def ft_load(path: str) -> any:
    """
    This function takes a path on a format string (URL), checks if the object
    is a JPG or JPEG image, then returns its dimensions.
    """
    if os.path.exists(path):
        _, extension = os.path.splitext(path)
        if extension.lower() in [".jpeg", ".jpg"]:
            try:
                with Image.open(path) as img:
                    img_rgb = img.convert(
                        "RGB"
                    )  # on convertit l'image pixel par pixel en RGB
                    image_array = np.array(
                        img_rgb
                    )  # l'image est convertie ensuite en array
                    print(f"The shape of image is: {image_array.shape}")
                    return image_array
            except IOError:
                print("Error opening this file.")
                return ()
        else:
            print("This file format isn't authorized")
            return ()
    else:
        print("This path doesn't exist")
        return ()
