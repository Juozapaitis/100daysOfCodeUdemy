import colorgram

colors = colorgram.extract('painting.jpg', 6)
color_palette = []

for count in range(len(color_list)):
    rgb = color_list[count]
    color = rgb.rgb
    color_palette.append(color)