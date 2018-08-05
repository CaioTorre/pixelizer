import numpy as np 
import math
from PIL import Image, ImageDraw
import sys
import imageio

import argvParser as parser

valid_args = ['-w', '-h', '-s', '-B']
image_path = sys.argv[1]
# image_path = parser.getNextValue(sys.argv
print('Fetching image '+sys.argv[1])
current_image = imageio.imread(image_path)

# pixel_width = int(sys.argv[2])
pixel_width = int(parser.getNextValue(sys.argv, '-w', current_image.shape[0]))
pixel_height = int(parser.getNextValue(sys.argv, '-h', current_image.shape[1]))

color_samples = int(parser.getNextValue(sys.argv, '-s', 256))
color_step = color_samples / 256  

size_out = 1 - int(parser.exists(sys.argv, '-B'))

if size_out == 1:
    image_out = np.uint8(np.zeros([pixel_width, pixel_height, 4]))
else:
    image_out = np.uint8(np.zeros(current_image.shape))

# if len(sys.argv) > 4:
    # pixel_height = int(sys.argv[3])
    # if sys.argv[4] == '--small':
        # size_out = 1
        # image_out = np.uint8(np.zeros([pixel_width, pixel_height, 3]))
    # elif sys.argv[4] == '--big':
        # size_out = 0
        # image_out = np.uint8(np.zeros(current_image.shape))
    # else:
        # size_out = -1
        # fail_message = sys.argv[4]
# else:
    # pixel_height = pixel_width
    # if sys.argv[3] == '--small':
        # size_out = 1
        # image_out = np.uint8(np.zeros([pixel_width, pixel_height, 4]))
    # elif sys.argv[3] == '--big':
        # size_out = 0
        # image_out = np.uint8(np.zeros(current_image.shape))
    # else:
        # size_out = -1
        # fail_message = sys.argv[3]

if size_out != -1:
    rec_width_d = int(current_image.shape[0]/(pixel_width))
    rec_height_d = int(current_image.shape[1]/(pixel_height))

    #print(repr(pixel_width)+'x'+repr(pixel_height))

    if size_out == 1:
        for x in range(pixel_width):
            for y in range(pixel_height):
                for c in range(4):
                    #print("x="+repr(x)+"; y="+repr(y)+"; c="+repr(c))
                    cx = x*rec_width_d
                    cy = y*rec_height_d
                    image_out[x,y,c] = min(255, math.floor(np.average(current_image[cx:cx+rec_width_d, cy:cy+rec_height_d, c]) * color_step + 0.5) / color_step)
    else:
        for x in range(pixel_width):
            for y in range(pixel_height):
                for c in range(4):
                    #print("x="+repr(x)+"; y="+repr(y)+"; c="+repr(c))
                    cx = x*rec_width_d
                    cy = y*rec_height_d
                    image_out[cx:cx+rec_width_d,cy:cy+rec_height_d,c] = min(255, math.floor(np.average(current_image[cx:cx+rec_width_d, cy:cy+rec_height_d, c]) * color_step + 0.5) / color_step)

    if size_out == 1:
        imageio.imwrite(image_path[0:-4]+'_'+repr(pixel_width)+'x'+repr(pixel_height)+'_small.png', image_out)
    else:
        imageio.imwrite(image_path[0:-4]+'_'+repr(pixel_width)+'x'+repr(pixel_height)+'_big.png', image_out)

    print("done!")
else:
    print("unknown option \""+fail_message+"\"")