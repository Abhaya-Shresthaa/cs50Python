import sys

from PIL import Image

images = []

for arg in sys.argv[1:]: # as the first one is the name of the program
    image = Image.open(arg)
    images.append(image)
    
images[0].save(
   # "name of image", save_all = true, append_images= [images[1]], duration = 200, loop = 0
)