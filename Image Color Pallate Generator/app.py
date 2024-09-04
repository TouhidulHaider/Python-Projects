import numpy as np 
from PIL import Image, ImageOps
from flask import Flask, render_template, request

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


def give_most_hex(file_path, code):
    img = Image.open(file_path).convert("RGB")
    size = img.size
    
    if size[0] >= 400 or size[1] >= 400:
        img = ImageOps.scale(image = img, factor = 0.2)

    img = ImageOps.posterize(img, 2)

    img_array = np.array(img)

    unique_colors = {}
    for column in img_array:
        for rgb in column:
            t_rgb = tuple(rgb)
            if t_rgb not in unique_colors:
                unique_colors[t_rgb] = 1
            if t_rgb in unique_colors:
                unique_colors[t_rgb] += 1

    sorted_unique_colors = sorted(unique_colors.items(), key=lambda x:x[1], reverse=True)
    sorted_unique_colors = dict(sorted_unique_colors)

    value = list(sorted_unique_colors.keys())
    top_ten = value[0:10]

    if code == 'hex':
        hex_list = []
        for i in top_ten:
            hex = rgb_to_hex(i)
            hex_list.append(hex)
        return hex_list
    else:
        return top_ten




app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        f = request.files["file"]
        color_code = request.form['color_code']
        colors = give_most_hex(f.stream, color_code)
        return render_template("index.html", colors_list = colors, code = color_code)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)