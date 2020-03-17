#import img lib
from PIL import Image

img = Image.open('car.jpg')
img.show()

#size of an image
img.size

#format of an image
img.format

#change the size of an image
img.thumbnail((300, 400))

#rotate an image
img.rotate(45).show()

#change to gray scale
gray_img = Image.open('car.jpg').convert('L')

#change the format of an image
img.save('car.png')
