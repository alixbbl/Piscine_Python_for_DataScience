from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
from PIL import Image

array = ft_load("landscape.jpg")
print(array)
new_array = ft_invert(array)
# new_array = ft_red(array)
# new_array = ft_green(array)
# new_array = ft_blue(array)
# new_array = ft_grey(array)
# new_array = print(ft_invert.__doc__)

image_to_display = Image.fromarray(new_array)
image_to_display.show()
