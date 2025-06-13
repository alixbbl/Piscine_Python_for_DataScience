import numpy as np
from load_image import ft_load
from PIL import Image


def zoom_image(path_img, start_row, end_row, start_col, end_col):
    """
    Load an image, slice it to the specified region, and convert that region
    to grayscale.

    :param path_img: Path to the image file.
    :param start_row: Start index for rows.
    :param end_row: End index for rows.
    :param start_col: Start index for columns.
    :param end_col: End index for columns.
    :return: A NumPy array of the sliced and grayscaled region.
    """

    img_load_array = ft_load(path_img)
    print(img_load_array)

    img_load = Image.fromarray(img_load_array)
    image_zoomed = img_load.crop((start_col, start_row, end_col, end_row))
    image_gray_zoomed = image_zoomed.convert("L")
    np_image = np.array(image_gray_zoomed)
    np_image_reshaped = np.expand_dims(np_image, axis=-1)

    print(
        f"New shape after slicing: {np_image_reshaped.shape} or \
            ({end_row - start_row}, {end_col - start_col})"
    )
    print(np_image_reshaped)
    return np_image_reshaped


def main():
    new_image = zoom_image("animal.jpeg", 100, 500, 100, 500)
    Image.fromarray(new_image[:, :, 0]).show()


if __name__ == "__main__":
    main()
