from load_image import ft_load
from pimp_image import ft_invert
from PIL import Image
# from pimp_image import ft_blue
# from pimp_image import ft_green
# from pimp_image import ft_grey
# from pimp_image import ft_red


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
