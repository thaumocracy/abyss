from PIL import Image, ImageDraw, ImageFont

im = Image.open('image_without.jpg')
width, height = im.size

draw = ImageDraw.Draw(im)
text = "BIG ASS PICTURE"

font = ImageFont.truetype('arial.ttf', 36)
textwidth, textheight = draw.textsize(text, font)

# calculate the x,y coordinates of the text
margin = 10
x = width - textwidth - margin
y = height - textheight - margin

# draw watermark in the bottom right corner
draw.text((x, y), text, font=font)
im.show()

# Save watermarked image
im.save('image_with.jpg')
