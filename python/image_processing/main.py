from PIL import Image, ImageFilter


def imgBlurred():
    img = Image.open('./snorlax.jpg')
    filteredImg = img.filter(ImageFilter.BLUR)
    filteredImg.save(f'{img.filename}_blur.png', 'png')


def imgGrey():
    img = Image.open('./snorlax.jpg')
    filteredImg = img.convert('L')
    filteredImg.save(f'{img.filename}_grey.png', 'png')


imgBlurred()
imgGrey()
