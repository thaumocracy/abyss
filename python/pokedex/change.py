import os
import sys
from PIL import Image


input_folder = sys.argv[1]
output_folder = sys.argv[2]


if not os.path.exists(output_folder):
    os.makedirs(output_folder)

arr = os.listdir(input_folder)

for img in arr:
    image = Image.open(f'./{input_folder}/{img}')
    clean_name = os.path.splitext(img)[0]
    image.save(f'./{output_folder}/{clean_name}.png', 'png')
