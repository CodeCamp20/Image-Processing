#import pillow
from PIL import Image

img = Image.open('car.jpg')
#print(img.mode)

box = (150, 200, 600, 600)
crop_img = img.crop(box) #left, upper, right, lower
#crop_img.show()


flip_img = img.transpose(Image.ROTATE_270)
flip_img.show()
