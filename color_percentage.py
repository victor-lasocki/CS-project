from PIL import Image
from math import pi

LaTeX = True

def calculate_color_percentage(image_path, target_color):
    image = Image.open(image_path)
    image = image.convert("RGB")

    width, height = image.size
    total_pixels = width * height
    target_pixels = 0

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            if (r, g, b) == target_color:
                target_pixels += 1

    percentage = (target_pixels / total_pixels) * 100

    return percentage

if not LaTeX:
    for i in range(8, 129, 8):
        image_path = f"/users/eleves-a/2021/victor.lasocki/1-radius/1-radius-{i}-result.png"
        target_color = (255, 255, 255)

        percentage_white = calculate_color_percentage(image_path, target_color)
        percentage_blue = round((100 - percentage_white), 2)

        print(f"Percentage of blue in the image 1-radius-{i}: {percentage_blue}%")

if LaTeX:
    for i in range(8, 129, 8):
        image_path = f"/users/eleves-a/2021/victor.lasocki/1-radius/1-radius-{i}-result.png"
        target_color = (255, 255, 255)

        percentage_white = calculate_color_percentage(image_path, target_color)
        percentage_blue = round((100 - percentage_white), 2)

        print(f"{i} & {round(((i**2 * pi)*100)/(256**2), 2)}% & {percentage_blue}% \\\\")
