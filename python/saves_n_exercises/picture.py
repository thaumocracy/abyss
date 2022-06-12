#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

zero = " "
one = "*"

for row in picture:
  content = ""
  for item in row:
    if item is 0:
      content += zero
    elif item is 1:
      content += one
  print(content)
