from PIL import Image, ImageOps
import numpy as np
from cv2 import imshow, waitKey, destroyAllWindows

file_path = "C:/Users/HP/Pictures/messi sachin.jpg"

img = Image.open(file_path).convert("RGB")
size = img.size

if size[0] >= 400 or size[1] >= 400:
    img = ImageOps.scale(image = img, factor = 0.2)

elif size[0] >= 600 or size[1] >= 600:
    img = ImageOps.scale(image = img, factor = 0.4)

elif size[0] >= 800 or size[1] >= 800:
    img = ImageOps.scale(image = img, factor = 0.5)

elif size[0] >= 1200 or size[1] >= 1200:
    img = ImageOps.scale(image = img, factor = 0.6)

img = ImageOps.posterize(img, 2)

img_array = np.array(img)

print(size)
print(img.size)

# imshow("Image", img_array)
# waitKey(0)
# destroyAllWindows()

unique_colors = {}
for column in img_array:
    for rgb in column:
        t_rgb = tuple(rgb)
        if t_rgb not in unique_colors:
            unique_colors[t_rgb] = 1
        if t_rgb in unique_colors:
            unique_colors[t_rgb] += 1

print(unique_colors)
sorted_unique_colors = sorted(unique_colors.items(), key=lambda x:x[1], reverse=True)
sorted_unique_colors = dict(sorted_unique_colors)
print(sorted_unique_colors)

value = list(sorted_unique_colors.keys())
top_ten = value[0:10]

print(top_ten)